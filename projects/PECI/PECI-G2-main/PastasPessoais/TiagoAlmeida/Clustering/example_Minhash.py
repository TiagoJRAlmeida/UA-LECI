from minhash_functions import *

default_test_names = ["Teste", "Hello"]
test_names = ["Teste1", "Testee1", "Hello1", "Helloo1", "Teste1"]
clustering = dict()
similarity_cache = dict()
seen_names = set()

def cached_similarity(name1, name2):
    key = tuple(sorted([name1, name2]))  # ordem não importa para Jaccard
    if key not in similarity_cache:
        similarity_cache[key] = jaccard_similarity(minhash_lookup[name1], minhash_lookup[name2])
    return similarity_cache[key]


# Cria um dicionário de lookup que relaciona nomes a assinaturas minhash
all_names = default_test_names + test_names
minhash_lookup = {name: get_minhash(name, 2) for name in all_names}


# Adiciona o nomes standard teste ao clustering
for default_test_name in default_test_names:
    if default_test_name in seen_names:
        continue
    else:
        clustering[default_test_name] = set()
        seen_names.add(default_test_name)


def update_cluster(cluster, key, new_name):
    # Lista de nomes no cluster, incluindo o novo nome e o central atual
    names = [key, new_name] + [name for name in cluster]

    # Calcula a similaridade média de cada nome com os restantes
    name_scores = {}
    for name in names:
        similarities = [
            cached_similarity(name, other)
            for other in names if other != name
        ]
        name_scores[name] = sum(similarities) / len(similarities)

    # Escolhe o nome com maior similaridade média como novo central
    best_name = max(name_scores, key=name_scores.get)
    print(f"Best Name: {best_name}")

    # Cria novo cluster com base no novo central
    new_cluster = set()
    for name, similarity in name_scores.items():
        if name != best_name:
            new_cluster.add(name)

    return best_name, new_cluster


# Adiciona os nomes teste ao clustering
for new_name in test_names:
    if new_name in seen_names:
        continue
    else:
        print(f"Current name --> {new_name}")
        print(f"Initial cluestering --> {clustering}")
        best_similarity = 0
        best_cluster = ""
        for cluster_key in clustering:
            if jaccard_similarity(minhash_lookup[new_name], minhash_lookup[cluster_key]) < 0.4:
                continue
            else:
                cluster_names = [cluster_key] + [n for n in clustering[cluster_key]]
                similarities = [
                    jaccard_similarity(minhash_lookup[new_name], minhash_lookup[other])
                    for other in cluster_names
                ]
                average_similarity = sum(similarities) / len(similarities)
                print(f"Similarity between <<{new_name}>> and cluster <<{cluster_key}>>: {average_similarity}")
                if average_similarity > best_similarity:
                    best_similarity = average_similarity
                    best_cluster = cluster_key

        print(f"Best choice: {best_cluster}")
        if best_similarity >= 0.7:
            new_key, new_cluster = update_cluster(clustering[best_cluster], best_cluster, new_name)
            clustering.pop(best_cluster)
            clustering[new_key] = new_cluster
        else:
            clustering[new_name] = set()
        seen_names.add(new_name)
        print(f"Updated cluestering --> {clustering}")
    print("\n")
    print("-"*60)