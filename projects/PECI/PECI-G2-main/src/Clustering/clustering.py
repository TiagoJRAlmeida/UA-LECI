from sentence_transformers import SentenceTransformer
from string_cleaning import clean_name, is_person_name
import Levenshtein
import numpy as np
from tqdm import tqdm
import faiss
from collections import defaultdict

LEGAL_PREFIX = {
    'plc', 'inc', 'company', 'tic', 'dis', 'sti', 'ltd', 'sirketi', 'ic', 'spa', 've', 'sa', 'ltdsti', 
    'san', 'as', 'pte', 'bv', 'ticaret', 'anonim', 'co', 'llc', 'gmbh', 'corp', 'ltda'
}

REGION_KEYWORDS = {
    # Full names
    'usa', 'us', 'uk', 'germany', 'greece', 'china', 'india', 'israel', 'egypt', 'uae',
    'turkey', 'saudi', 'france', 'spain', 'italy', 'canada', 'brazil', 'mexico', 'australia',
    'panama', 'japan', 'senegal', 'colombia', 'vietnam', 'indonesia', 'netherlands',
    'south africa', 'portugal', 'argentina', 'singapore', 'russia', 'poland', 'peru', 'chile',
    'morocco', 'algeria', 'kenya', 'tanzania', 'ghana', 'nigeria', 'costa rica', 'ecuador',
    'bolivia', 'uruguay', 'venezuela', 'honduras', 'guatemala', 'nicaragua', 'paraguay',
    'dominican', 'el salvador', 'lebanon', 'sri lanka', 'bangladesh', 'nepal', 'pakistan',
    'thailand', 'malaysia', 'myanmar', 'taiwan', 'hong kong', 'south korea', 'korea', 'mozambique',
    'angola', 'tunisia', 'libya', 'zambia', 'zimbabwe', 'cameroon', 'ethiopia', 'botswana',

    # Cities or custom regions
    'dubai', 'riyadh', 'jeddah', 'cairo', 'doha', 'abu dhabi', 'amman', 'santiago',
    'barcelona', 'madrid', 'guadalajara', 'monterrey', 'puebla', 'lyon', 'porto', 'lisbon',
    'paris', 'milan', 'milano', 'napoli', 'rome', 'athens', 'sofia', 'bucharest', 'vienna',
    'warsaw', 'zagreb', 'brussels', 'oslo', 'stockholm', 'copenhagen', 'geneva', 'lausanne',
    'luxembourg', 'shanghai', 'beijing', 'shenzhen', 'qingdao', 'xiamen', 'tianjin',

    # ISO Alpha-2 country codes
    'us', 'fr', 'de', 'pt', 'es', 'it', 'nl', 'be', 'se', 'no', 'fi', 'dk', 'pl', 'gr',
    'ro', 'bg', 'cz', 'hu', 'sk', 'si', 'at', 'ch', 'ie', 'ru', 'tr', 'cn', 'jp', 'kr', 'in',
    'id', 'th', 'my', 'vn', 'sg', 'ph', 'bd', 'pk', 'il', 'eg', 'sa', 'ae', 'qa', 'kw', 'dz',
    'ma', 'tn', 'ng', 'gh', 'za', 'zm', 'zw', 'cm', 'ke', 'tz',

    # ISO Alpha-3 codes (and common short customs abbreviations)
    'usa', 'mex', 'can', 'esp', 'bra', 'deu', 'fra', 'ita', 'prt', 'nld', 'bel', 'che', 'swe',
    'nor', 'fin', 'dnk', 'pol', 'grc', 'rou', 'bgr', 'cze', 'hun', 'svk', 'svn', 'aut', 'irl',
    'gbr', 'rus', 'tur', 'chn', 'jpn', 'kor', 'ind', 'idn', 'tha', 'mys', 'vnm', 'sgp', 'phl',
    'pak', 'bgd', 'isr', 'egy', 'sau', 'are', 'qat', 'kwt', 'dza', 'mar', 'tun', 'nga', 'gha',
    'zaf', 'zmb', 'zwe', 'cmr', 'ken', 'tza',

    # Seen in the clusters
    'esp', 'pt', 'po', 'sh', 'sur', 'sor', 'ne', 'lim', 'sen', 'del', 'mex'
}


def extract_regions(name):
    tokens = name.split()
    regions = {t for t in tokens if t in REGION_KEYWORDS}
    if not regions:
        return {"default"}

    # Optional: Prioritize last token if it's a region
    if tokens[-1] in REGION_KEYWORDS:
        return {tokens[-1]}  # force clear region tag

    return regions


# EXAMPLE: Given the cluster:
# [
#     "hellmann worldwide logistics china usa",
#     "hellmann worldwide logistics china",
#     "hellmann worldwide logistics usa",
#     "hellmann worldwide logistics india"
# ]

# It will divide like:
# [
#     ["hellmann worldwide logistics china usa", "hellmann worldwide logistics china", "hellmann worldwide logistics usa"],
#     ["hellmann worldwide logistics india"]
# ]
def postprocess_by_region(clusters):
    new_clusters = []

    for cluster in clusters:
        name_to_regions = {name: extract_regions(name) for name in cluster}

        # Group names by region overlap
        region_groups = []
        assigned = set()

        for name, regions in name_to_regions.items():
            if name in assigned:
                continue
            group = [name]
            assigned.add(name)

            for other_name, other_regions in name_to_regions.items():
                if other_name in assigned:
                    continue
                if regions & other_regions:  # any shared region
                    group.append(other_name)
                    assigned.add(other_name)

            region_groups.append(group)

        new_clusters.extend(region_groups)

    return new_clusters


def get_core_prefix(name, max_tokens=2):
    tokens = [t for t in name.split() if t not in LEGAL_PREFIX]
    return " ".join(tokens[:max_tokens])


def shared_prefix(a, b, n=2):
    return get_core_prefix(a, n) == get_core_prefix(b, n)


def weighted_token_jaccard(a, b):
    tokens_a = set(a.split())
    tokens_b = set(b.split())

    intersection = 0
    union = tokens_a | tokens_b

    for token in tokens_a & tokens_b:
        if token in LEGAL_PREFIX or token in REGION_KEYWORDS:
            intersection += 0.2  # small weight
        else:
            intersection += 1.0  # full weight

    return intersection / len(union)


def normalized_levenshtein_core(name1, name2):
    # Remove legal terms
    t1 = " ".join([t for t in name1.split() if t not in LEGAL_PREFIX and t not in REGION_KEYWORDS])
    t2 = " ".join([t for t in name2.split() if t not in LEGAL_PREFIX and t not in REGION_KEYWORDS])
    if not t1 or not t2:
        return 1.0  # prevent false match on empty core
    dist = Levenshtein.distance(t1, t2)
    return dist / max(len(t1), len(t2))


def combined_similarity(name1, name2):
    lev_sim = 1 - normalized_levenshtein_core(name1, name2)
    jac_sim = weighted_token_jaccard(name1, name2)
    return 0.7 * lev_sim + 0.3 * jac_sim


def refine_noisy_cluster(cluster):
    refined = []
    for name in cluster:
        added = False
        for group in refined:
            if all(combined_similarity(name, other) >= 0.75 for other in group):
                group.append(name)
                added = True
                break
        if not added:
            refined.append([name])
    return refined


# NOTE: names argument must be a set of already cleaned names.
# base_clusters argument must also contain names in their cleaned form
def create_clusters(names=None, similarity_threshold=0.75, base_clusters=[]):
    if not names:
        return base_clusters

    names = {name for name in names if name.strip()}

    # Flatten base clusters and store index
    base_clustered_names = set()
    base_cluster_map = {}
    for idx, cluster in enumerate(base_clusters):
        for name in cluster:
            base_clustered_names.add(name)
            base_cluster_map[name] = idx

    # Why create and use "all_name" instead of just remaining_names?
    # Because we also want to embed the base clustered names, so that they are indexed and
    # can appear in the query results.
    # This way, we can also use the expand upon the base clusters.  
    remaining_names = names - base_clustered_names
    all_names = list(base_clustered_names) + list(remaining_names)

    # Step 1: Get embeddings
    #print("Calculating embeddings...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(all_names, convert_to_numpy=True)

    # Step 2: Normalize embeddings
    #print("Normalizing embeddings...")
    faiss.normalize_L2(embeddings)

    # Step 3: Index embeddings
    #print("Indexing embeddings...")
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    clustered = [False] * len(all_names)
    clusters = [list(cluster) for cluster in base_clusters]

    #print(f"Building Clustering...\n")
    for i in tqdm(range(len(all_names)), desc="Adding Names to Clusters", unit="name"):
        # Allow others to attach to base, but not re-process base elements
        if all_names[i] in base_clustered_names:
            continue

        if clustered[i]:
            continue

        new_name = all_names[i]
        embedding = embeddings[i]

        D, I = index.search(np.expand_dims(embedding, axis=0), 1000)

        cluster = [new_name]
        best_match = None
        best_score = 0

        for idx, score in zip(I[0], D[0]):
            candidate_name = all_names[idx]
            if idx == i or clustered[idx]:
                continue
            
            adjusted_threshold = 0.95 if is_person_name(new_name) or is_person_name(candidate_name) else similarity_threshold


            if score >= adjusted_threshold and shared_prefix(new_name, candidate_name):
                if candidate_name in base_clustered_names:
                    if score > best_score:
                        best_score = score
                        best_match = base_cluster_map[candidate_name] # Best match is an index to the clusters list!
                else:
                    cluster.append(candidate_name)
                    clustered[idx] = True

        if best_match is not None:
            clusters[best_match].extend(cluster)
        else:
            clusters.append(cluster)
        clustered[i] = True

    #print("Refining noisy clusters with Levenshtein (if necessary)...")
    final_clusters = []
    for cluster in clusters:
        if len(cluster) > 5:  # Filter only on bigger clusters
            refined = refine_noisy_cluster(cluster)
            final_clusters.extend(refined)
        else:
            final_clusters.append(cluster)

    return final_clusters


# NOTE: This function returns 3 things:
# 1. The synonym clusters, a list of lists, where each list is a cluster 
# 2. A set of all unique names in the synonym clusters
# 3. A dictionary that maps the index of each cluster to its standard name 
# (This 3rd variable returned will be usefull in the "Step 4: Creating final synonym map" of the main file)
def create_ground_truth_synonym_clusters(synonyms_map):
    synonym_clusters = {}
    cluster_index_standard_name_map = {}
    all_names = set()

    for variant_name in synonyms_map.keys():
        if len(synonyms_map[variant_name]) > 1:
            continue
        
        standard_name = list(synonyms_map[variant_name].keys())[0] 
        if len(synonyms_map[variant_name][standard_name]) > 1:
            continue

        identification_number = synonyms_map[variant_name][standard_name][0][0]
        cluster = synonym_clusters.setdefault(identification_number, {
            "standard_name": standard_name,
            "synonyms": set()
        })
        cluster["synonyms"].add(variant_name)
        all_names.update([variant_name, standard_name])
    
    final_clusters = []
    for idx, identification_number in enumerate(synonym_clusters):
        cluster = synonym_clusters[identification_number]
        cleaned_cluster = cluster["synonyms"]
        cleaned_cluster.add(clean_name(cluster["standard_name"]))
        final_clusters.append(list(cleaned_cluster))
        cluster_index_standard_name_map[idx] = cluster["standard_name"]

    return final_clusters, all_names, cluster_index_standard_name_map
