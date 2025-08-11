import pandas as pd
import json
import pickle
import os
from minhash_functions import *
from table_functions import *
import time
from functools import lru_cache

start_time = time.time()


print("Reading Unique Standard Names...")
with open('../UniqueNamesScripts/Standard-Unique_Names.json', 'r', encoding="utf-8") as file:
    Standard_Unique_Names = json.load(file)

print("Reading Unique Departure Names...")
with open('../UniqueNamesScripts/Departure-Unique_Names.json', 'r', encoding="utf-8") as file:
    Departure_Unique_Names = json.load(file)

print("Reading Unique Transport Names...")
with open('../UniqueNamesScripts/Transport-Unique_Names.json', 'r', encoding="utf-8") as file:
    Transport_Unique_Names = json.load(file)


# Cria um dicionário de lookup que relaciona nomes a assinaturas minhash
def createMinHashLookup():
    all_names = set(Standard_Unique_Names) | set(Transport_Unique_Names) | set(Transport_Unique_Names)
    minhash_lookup = {name: get_minhash(name, 2) for name in all_names}
    
    with open("Minhash_Lookup.pkl", "wb") as f:
        pickle.dump(minhash_lookup, f)


if not os.path.isfile("Minhash_Lookup.pkl"):
    print("\nCreating Minhash Lookup dictionary...")
    createMinHashLookup()
    print("Minhash Lookup dictionary created!")
with open("Minhash_Lookup.pkl", "rb") as f:
    minhash_lookup = pickle.load(f)
    

@lru_cache(maxsize=100000)
def cachedSimilarity(name1, name2):
    key1, key2 = sorted([name1, name2])
    return jaccard_similarity(minhash_lookup[key1], minhash_lookup[key2])


def updateCluster(cluster, key, new_name):
    # Lista de nomes no cluster, incluindo o novo nome e o central atual
    names = [key, new_name] + [name for name in cluster]

    # Calcula a similaridade média de cada nome com os restantes
    name_scores = {}
    for name in names:
        similarities = [
            cachedSimilarity(name, other)
            for other in names if other != name
        ]
        name_scores[name] = sum(similarities) / len(similarities)

    # Escolhe o nome com maior similaridade média como novo central
    best_name = max(name_scores, key=name_scores.get)

    # Cria novo cluster com base no novo central
    new_cluster = set()
    for name, similarity in name_scores.items():
        if name != best_name:
            new_cluster.add(name)

    return best_name, new_cluster


def createClusters(stopwords=set()):
    clusters = dict()
    seen_names = set()

    # Adiciona o nomes standard teste ao clustering
    print("\nAdding Unique Standard Names to the clusters...")
    count = 0
    for standard_name in Standard_Unique_Names:
        count += 1
        if standard_name in seen_names:
            continue
        else:
            clusters[standard_name] = set()
            seen_names.add(standard_name)
        print(f"\rName Count: {count}", end="")
    print("\nDone!")


    print("\n")
    print("-"*60)


    # Adiciona os nomes Departure ao clustering
    print("\nAdding Unique Departure Names to the clusters...")
    count = 0
    for departure_name in Departure_Unique_Names:
        count += 1
        if departure_name in seen_names or departure_name in stopwords:
            continue
        else:
            best_similarity = 0
            best_cluster = ""
            for center_name in clusters:
                if jaccard_similarity(minhash_lookup[departure_name], minhash_lookup[center_name]) < 0.4:
                    continue
                else:
                    cluster_names = [center_name] + [n for n in clusters[center_name]]
                    similarities = [
                        jaccard_similarity(minhash_lookup[departure_name], minhash_lookup[other])
                        for other in cluster_names
                    ]
                    average_similarity = sum(similarities) / len(similarities)
                    if average_similarity > best_similarity:
                        best_similarity = average_similarity 
                        best_cluster = center_name
            if best_similarity >= 0.7:
                new_key, new_cluster = updateCluster(clusters[best_cluster], best_cluster, departure_name)
                clusters.pop(best_cluster)
                clusters[new_key] = new_cluster
            else:
                clusters[departure_name] = set()
            seen_names.add(departure_name)
        print(f"\rName Count: {count}", end="")
    print("\nDone!")


    print("\n")
    print("-"*60)


    # Adiciona os nomes Transport ao clustering
    print("\nAdding Unique Transport Names to the clusters...")
    count = 0
    for transport_name in Transport_Unique_Names:
        count += 1
        if transport_name in seen_names or transport_name in stopwords:
            continue
        else:
            best_similarity = 0
            best_cluster = ""
            for center_name in clusters:
                if jaccard_similarity(minhash_lookup[transport_name], minhash_lookup[center_name]) < 0.4:
                    continue
                cluster_names = [center_name] + [n for n in clusters[center_name]]
                similarities = [
                    jaccard_similarity(minhash_lookup[transport_name], minhash_lookup[other])
                    for other in cluster_names
                ]
                average_similarity = sum(similarities) / len(similarities)
                if average_similarity > best_similarity:
                    best_similarity = average_similarity 
                    best_cluster = center_name
            if best_similarity >= 0.7:
                new_key, new_cluster = updateCluster(clusters[best_cluster], best_cluster, transport_name)
                clusters.pop(best_cluster)
                clusters[new_key] = new_cluster
            else:
                clusters[transport_name] = set()
            seen_names.add(transport_name)
        print(f"\rName Count: {count}", end="")
    print("\nDone!")

    name_count = 0
    for center_name in clusters:
        name_count += len(clusters[center_name])
    print(f"Number of names in Clusters (center name included): {name_count}")

    # Ordenar os clusters por número de elementos (excluindo "value")
    sorted_clusters = dict(
        sorted(clusters.items(), key=lambda item: len(item[1]) - 1, reverse=True)
    )

    # Converter todos os sets em listas antes de guardar
    json_friendly_clusters = {k: list(v) for k, v in sorted_clusters.items()}

    with open(f"Clustering.json", "w", encoding="utf-8") as f:
            json.dump(json_friendly_clusters, f, ensure_ascii=False, indent=4)


createClusters()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"\nExecution time: {elapsed_time:.2f} seconds <=> {(elapsed_time/60.0):.2f} minutes <=> {(int(elapsed_time/3600) + ((elapsed_time/3600 - int(elapsed_time/3600))*60)/100):.2f} hours")

