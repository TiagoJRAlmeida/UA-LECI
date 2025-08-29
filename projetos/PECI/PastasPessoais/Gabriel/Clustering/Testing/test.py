import json
from strings_manipulation import * 
from minhash_functions import *
from remove_commonwords import remove_common

#Encontra o novo centroid do cluster
def find_centroid(names,map):
    # Calcula a similaridade média de cada nome com os restantes
    name_scores = {}
    for name in names:
        similarities = [jaccard_similarity(map[name],map[other]) for other in names if other != name]

        if len(similarities) > 0:
            name_scores[name] = sum(similarities) / len(similarities)
        else:
            name_scores[name] = 0
    
    return max(name_scores, key=name_scores.get)

with open("test_data.json","r") as f:
    test = json.loads(f.read())

names = {j for i in test.values() for j in i}

keys = {i for i in test.keys()}

minhashes = {}
for i in names:
    if i not in minhashes:
        minhashes[i] = get_minhash(remove_common(i))

for i in keys:
    if i not in minhashes:
        minhashes[i] = get_minhash(remove_common(i))

std_list = {i for i in keys}
std_dict = dict()

#Creates initial clusters
for i in keys:
    std_dict[i] = {"names":list(),
                   "centroid":i}
count = 0

#names = names | keys
#Insert names into clusters
for i in names:
    print(f"\rCurrent Percentage : % {(count/len(names))*100}", end="")
    max_distance = 0
    max_std_name = str()

    for j in std_list:
        if jaccard_similarity(minhashes[i],minhashes[std_dict[j]["centroid"]]) <= 0.4:
            continue
        else:
            cluster_names = [j] + [n for n in std_dict[j]["names"]]

            similarities = [jaccard_similarity(minhashes[i], minhashes[other]) for other in cluster_names]

            average_similarity = sum(similarities) / len(similarities)

            if average_similarity >= max_distance:
                max_distance = average_similarity
                max_std_name = j
    
    if max_distance >= 0.5:
        if i not in std_dict[max_std_name]["names"]:
            std_dict[max_std_name]["names"].append(i)
            count+=1
    else:
        std_list.add(i)
        std_dict[i] = {"names":list(),
                   "centroid":i}
        count+=1
        continue

    centroid = find_centroid(std_dict[max_std_name]["names"] + [max_std_name],minhashes)
    if centroid != max_std_name:
        std_dict[max_std_name]["centroid"] = centroid

std_dict = {k:{"names":std_dict[k]["names"],"centroid":std_dict[k]["centroid"]} for k in sorted({i for i in std_dict.keys()})}

with open("train_data.json","w") as f:
    json.dump(std_dict, f,indent=6)