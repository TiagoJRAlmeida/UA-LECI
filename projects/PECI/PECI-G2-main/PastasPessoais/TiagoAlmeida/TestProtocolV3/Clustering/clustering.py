from sentence_transformers import SentenceTransformer
from strings_manipulation import clean_name, is_person_name
import numpy as np
from tqdm import tqdm
import faiss
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
people_names_file_path = os.path.join(BASE_DIR, "../AuxiliaryFiles/people_names.txt")


def create_clusters(names=None, similarity_threshold=0.90, base_clusters=[]):
    if not names:
        return base_clusters

    names_file = open(people_names_file_path, 'w')

    # Flatten base clusters and store index
    cleaned_base_clustered_names = set()
    cleaned_base_cluster_map = {}
    for idx, cluster in enumerate(base_clusters):
        for name in cluster:
            cleaned_name = clean_name(name)
            cleaned_base_clustered_names.add(cleaned_name)
            cleaned_base_cluster_map[cleaned_name] = idx


    # Step 1: Preprocess names
    cleaned_names = set([clean_name(name) for name in names])

    # Why create and use "all_name" instead of just remaining_names?
    # Because we also want to embed the base clustered names, so that they are indexed and
    # can appear in the query results.
    # This way, we can also use the expand upon the base clusters.  
    cleaned_remaining_names = cleaned_names - cleaned_base_clustered_names
    cleaned_all_names = list(cleaned_base_clustered_names) + list(cleaned_remaining_names)

    # Step 2: Get embeddings
    print("Calculating embeddings...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(cleaned_all_names, convert_to_numpy=True)

    # Step 3: Normalize embeddings
    print("Normalizing embeddings...")
    faiss.normalize_L2(embeddings)

    # Step 4: Index embeddings
    print("Indexing embeddings...")
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    clustered = [False] * len(cleaned_all_names)
    clusters = [list(cluster) for cluster in base_clusters]

    print(f"Building Clustering...\n")
    for i in tqdm(range(len(cleaned_all_names)), desc="Adding Names to Clusters", unit="name"):
        # Allow others to attach to base, but not re-process base elements
        if cleaned_all_names[i] in cleaned_base_clustered_names:
            continue

        if clustered[i]:
            continue

        cleaned_new_name = cleaned_all_names[i] # new_name is a cleaned name
        embedding = embeddings[i]

        adjusted_threshold = similarity_threshold + (0.05 if is_person_name(cleaned_new_name) else 0.0)
        if is_person_name(cleaned_new_name):
            names_file.write(f"{cleaned_new_name}\n")

        D, I = index.search(np.expand_dims(embedding, axis=0), 1000)

        cluster = [cleaned_new_name]
        best_match = None
        best_score = 0

        for idx, score in zip(I[0], D[0]):
            cleaned_candidate_name = cleaned_all_names[idx]
            if idx == i or clustered[idx]:
                continue
                
            cleaned_candidate_len = len(cleaned_candidate_name)
            avg_len = (len(cleaned_new_name) + cleaned_candidate_len) / 2
            # adjusted_threshold += 0.05 if avg_len < 5 else 0.0

            if score >= adjusted_threshold:
                if cleaned_candidate_name in cleaned_base_clustered_names:
                    if score > best_score:
                        best_score = score
                        best_match = cleaned_base_cluster_map[cleaned_candidate_name] # Best match is an index to the clusters list!
                else:
                    cluster.append(cleaned_candidate_name)
                    clustered[idx] = True

        if best_match is not None:
            clusters[best_match].extend(cluster)
        else:
            clusters.append(cluster)
        clustered[i] = True

    print("\nClustering concluído.")
    return clusters



# NOTE: This function returns 3 things:
# 1. The synonym clusters, a list of lists, where each list is a cluster 
# 2. A set of all unique names in the synonym clusters
# 3. A dictionary that maps the index of each cluster to its standard name 
# (This 3rd variable returned will be usefull in the "Step 4: Creating final synonym map" of the main file)
def create_synonym_clusters(synonyms_map):
    synonym_clusters = {}
    cluster_index_standard_name_map = {}
    all_names = set()

    for name, (standard_name, identification_number) in synonyms_map.items():
        cluster = synonym_clusters.setdefault(identification_number, {
            "standard_name": standard_name,
            "synonyms": set()
        })
        cluster["synonyms"].add(name)
        all_names.update([name, standard_name])
    
    final_clusters = []
    for idx, identification_number in enumerate(synonym_clusters):
        cluster = synonym_clusters[identification_number]
        cleaned_cluster = {clean_name(n) for n in cluster["synonyms"]}
        cleaned_cluster.add(clean_name(cluster["standard_name"]))
        final_clusters.append(list(cleaned_cluster))
        cluster_index_standard_name_map[idx] = cluster["standard_name"]

    return final_clusters, all_names, cluster_index_standard_name_map
