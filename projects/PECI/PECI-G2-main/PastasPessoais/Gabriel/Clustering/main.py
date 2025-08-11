import pandas as pd
import json
import pickle
import os
from minhash_functions import *
import time
from functools import lru_cache

start_time = time.time()

with open("UniqueNames.txt","r", encoding="utf-8") as file:
    unique_names = set(file.read().split("\n"))

with open("sinonims.json","r") as f:
    sino = json.loads(f.read())

stdnames = {i for i in sino.keys()}
fnames = {j for i in sino.values() for j in i if len(i) > 0} | stdnames

# Cria um dicionário de lookup que relaciona nomes a assinaturas minhash
def createMinHashLookup():
    names = unique_names | stdnames
    minhash_lookup = {name: get_minhash(name, 2) for name in names}
    
    with open("Minhash_Lookup.pkl", "wb") as f:
        pickle.dump(minhash_lookup, f)


if not os.path.isfile("Minhash_Lookup.pkl"):
    print("\nCreating Minhash Lookup dictionary...")
    createMinHashLookup()
    print("Minhash Lookup dictionary created!")
    
with open("Minhash_Lookup.pkl", "rb") as f:
    minhash_lookup = pickle.load(f)


similarity_cache = dict()


@lru_cache(maxsize=100000)
def cachedSimilarity(name1, name2):
    key1, key2 = sorted([name1, name2])
    return jaccard_similarity(minhash_lookup[key1], minhash_lookup[key2])


def updateCluster(cluster, key, new_name):
    # Lista de nomes no cluster, incluindo o novo nome e o central atual
    names = [key, new_name] + [name for name in cluster]
    best_name = key

    # Calcula a similaridade média de cada nome com os restantes
    name_scores = {}
    for name in names:
        similarities = [
            cachedSimilarity(name, other)
            for other in names if other != name
        ]

        if len(similarities) > 0:
            name_scores[name] = sum(similarities) / len(similarities)

    # Escolhe o nome com maior similaridade média como novo central
    if len(name_scores) > 0:
        best_name = max(name_scores, key=name_scores.get)

    # Cria novo cluster com base no novo central
    new_cluster = set()
    for name, similarity in name_scores.items():
        if name != best_name:
            new_cluster.add(name)

    return best_name, new_cluster


def createClusters():
    clusters = sino
    print(clusters)

    # Adiciona os nomes ao clustering
    print("\nAdding Unique Names to the clusters...")
    count = 0
    for name in unique_names:
        count += 1
        print(count)

        best_similarity = 0
        best_cluster = ""

        for center_name in clusters.keys():      
            if jaccard_similarity(minhash_lookup[name],minhash_lookup[center_name]) > best_similarity:
                best_similarity = jaccard_similarity(minhash_lookup[name],minhash_lookup[center_name]) 
                best_cluster = center_name

        if best_similarity >= 0.8:
            clusters[best_cluster].append(name)
        else:
            clusters[name] = list()
            
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
print(f"\nExecution time: {elapsed_time:.2f} seconds <=> {(elapsed_time/60.0):.2f} minutes <=> {(elapsed_time/3600.0):.2f} hours")