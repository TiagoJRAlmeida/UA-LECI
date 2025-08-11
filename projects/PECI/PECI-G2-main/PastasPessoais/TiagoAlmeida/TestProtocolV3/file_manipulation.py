import os
import json
from datasketch import MinHashLSH
from strings_manipulation import * 
from minhash_functions import *


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_dict_id_to_name(standard_data_frame):
    id_to_name_map = {"Repetidos": []}
    
    for _, row in standard_data_frame.iterrows():
        name = str(row["name"])
        short_name = str(row["short_name"])
        identification_number = str(row["identification_number"])
        
        if identification_number not in id_to_name_map:
            id_to_name_map[identification_number] = [name, short_name]
        else:
            id_to_name_map["Repetidos"].append(identification_number)
        
    return id_to_name_map


def create_dict_name_to_id(standard_data_frame):
    name_to_id_map = {}

    for _, row in standard_data_frame.iterrows():
        name = str(row["name"])
        short_name = str(row["short_name"])
        identification_number = str(row["identification_number"])

        for key in [name, short_name]:
            if key not in name_to_id_map:
                name_to_id_map[key] = {identification_number}
            else:
                name_to_id_map[key].add(identification_number)

    # Converter sets em listas para serializar com JSON
    name_to_id_map = {k: list(v) for k, v in name_to_id_map.items()}

    return name_to_id_map


def create_dict_standard_words():
    # Read Standard unique words
    standard_unique_names_file_path = os.path.join(BASE_DIR, "UniqueNamesScripts/Standard-unique_names_count.json")
    with open((standard_unique_names_file_path), 'r', encoding="utf-8") as file:
        Standard_Unique_Names = json.load(file)

    words_names = {}
    
    for name in Standard_Unique_Names:
        words = clean_name(name).split()
        for word in words:
            if word not in words_names:
                words_names[word] = set(name)
            else:
                words_names[word].add(name)

    words_names = {k: list(v) for k, v in words_names.items()}
    return words_names


def create_set_unique_words(standard_words_map):
    unique_words = set()
    for word in standard_words_map:
        if not word.isnumeric() and len(word) >= 3 and len(standard_words_map[word]) <= 7:
            unique_words.add(word)
    return unique_words


def create_minHashLSH_table(standard_data_frame):
    lsh = MinHashLSH(threshold=0.8, num_perm=128)   # Criar um índice LSH para encontrar nomes similares rapidamente 
    minhashes = {}  # Dicionário para armazenar MinHashes
    for _, row in standard_data_frame.iterrows():
        standard_name = str(row["name"])
        if standard_name not in minhashes:
            minhashes[standard_name] = get_minhash(clean_name(standard_name))
            lsh.insert(standard_name, minhashes[standard_name])
    return lsh


def create_dict_short_name_to_name(standard_data_frame):
    short_name_to_name_map = {}
    
    for _, row in standard_data_frame.iterrows():
        name = str(row["name"])
        short_name = str(row["short_name"])
        
        if short_name not in short_name_to_name_map:
            short_name_to_name_map[short_name] = set()
            short_name_to_name_map[short_name].add(name)
        else:
            short_name_to_name_map[short_name].add(name)
    
    for key in short_name_to_name_map:
        if len(short_name_to_name_map[key]) > 1:
            print(key, short_name_to_name_map[key])

    return short_name_to_name_map