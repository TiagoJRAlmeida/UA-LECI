import pandas as pd
import Levenshtein

default_test_names = ["Teste", "Hello"]
test_names = ["Teste1", "Testee1", "Hello1", "Helloo1", "Teste1"]
test_clustering = dict()
seen_names = set()

# Cria um dicionário de lookup que relaciona nomes a assinaturas minhash
all_names = default_test_names + test_names


# Adiciona o nomes standard teste ao clustering
for default_test_name in default_test_names:
    if default_test_name in seen_names:
        continue
    else:
        test_clustering[default_test_name] = {"value": 1.0}
        seen_names.add(default_test_name)


def update_cluster(cluster, key, new_name):
    names_values = [[key, 0], [new_name, 0]]
    for name in cluster:
        if name == "value":
            continue
        else:
            names_values.append([name, 0])
    
    best_name = ""
    best_similarity = 0
    for index, name in enumerate(names_values):
        name = name[0]
        if name == "value":
            continue
        else:
            similarity_sum = 0
            for other_name in names_values:
                other_name = other_name[0]
                if other_name == name or other_name == "value":
                    continue
                else:
                    similarity_sum += Levenshtein.distance(name, other_name)
            similarity = similarity_sum/(len(names_values) - 1)
            if similarity >= best_similarity:
                best_similarity = similarity
                best_name = name
            names_values[index] = [name, similarity]

    new_cluster = {"value": best_similarity}

    for index, name in enumerate(names_values):
        name = name[0]
        if name == best_name:
            continue
        else:
            new_cluster.update({name: names_values[index][1]})

    return best_name, new_cluster


# Adiciona os nomes teste ao clustering
for test_name in test_names:
    if test_name in seen_names:
        continue
    else:
        print(f"Current name {test_name}")
        limit_distance = (len(test_name) * 0.8)
        print(f"Limit Distance: {limit_distance}")
        print(f"Initial cluestering {test_clustering}")
        best_similarity = None
        best_name = ""
        for center_name in test_clustering:
            current_similatiry = Levenshtein.distance(center_name, test_name)
            print(f"Similarity between {center_name} and {test_name}: {current_similatiry}")
            if best_similarity == None or current_similatiry < best_similarity:
                best_similarity = current_similatiry 
                best_name = center_name
        print(f"Best choice: {best_name}")
        if best_similarity < limit_distance and best_similarity != 0:
            new_key, new_cluster = update_cluster(test_clustering[best_name], best_name, test_name)
            test_clustering.pop(best_name)
            test_clustering[new_key] = new_cluster
        else:
            test_clustering[test_name] = {"value": 1.0}
        seen_names.add(test_name)
        print(f"Updated cluestering {test_clustering}")
    print("\n")
    print("-"*60)