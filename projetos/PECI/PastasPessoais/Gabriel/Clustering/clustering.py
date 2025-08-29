import pandas as pd
import numpy as np
import json
import pickle
from datasketch import MinHashLSH
from strings_manipulation import * 
from minhash_functions import *
#from remove_commonwords import remove_common

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


#df_transport = pd.read_csv("D:/Projeto PECI/Transport_Document_Data.csv",sep=";")

with open("sinonims.json","r") as f:
    sino = json.loads(f.read())

fnames = {j for i in sino.values() for j in i if len(i) > 0}
#nfnames = list({i for i in df_transport["name"]})

#with open("UniqueNames.txt","w",encoding="utf-8") as file:
#    file.write("".join({i + '\n' for i in nfnames}))

with open("UniqueNames.txt","r", encoding="utf-8") as file:
    nfnames = file.read().split("\n")

nfnames.sort()

std_names = list({i for i in sino.keys()})
std_names.sort()

# Cria dicionário para armazenar MinHashes
'''print("Creating minhash table")

minhashes = {}
for i in fnames:
    if i not in minhashes:
        minhashes[i] = get_minhash(i)

for i in nfnames:
    if i not in minhashes:
        minhashes[i] = get_minhash(i)

for i in std_names:
    if i not in minhashes:
        minhashes[i] = get_minhash(i)

with open("minhash_nf.pkl", "wb") as f:
    pickle.dump(minhashes, f)

print("Finished creating minhash table")'''

with open("minhash_nf.pkl", "rb") as f:
    minhashes = pickle.load(f)

std_list = {i for i in std_names}
std_dict = dict()

#Creates initial clusters
for i in std_names:
    std_dict[i] = {"names":sino[i],
                   "centroid":i}
count = 0

#Insert names into clusters
for i in nfnames:
    print(f"\rCurrent Percentage : % {(count/len(nfnames))*100}", end="")
    max_distance = 0
    max_std_name = str()

    for j in std_list:
        if jaccard_similarity(minhashes[i],minhashes[j]) >= max_distance:
            max_distance = jaccard_similarity(minhashes[i],minhashes[j])
            max_std_name = j
    
    if max_distance >= 0.8:
        if i not in std_dict[max_std_name]["names"]:
            std_dict[max_std_name]["names"].append(i)
    else:
        std_list.add(i)
        std_dict[i] = {"names":list(),
                   "centroid":i}

    centroid = find_centroid(std_dict[max_std_name]["names"] + [max_std_name],minhashes)
    if centroid != max_std_name:
        std_dict[max_std_name]["centroid"] = centroid

    count+=1

with open("Clusters.json","w") as f:
    json.dump(std_dict, f,indent=6)
