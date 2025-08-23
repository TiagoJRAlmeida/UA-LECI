import json
import pickle
from datasketch import MinHashLSH
from TestProtocolV2.strings_manipulation import * 
from TestProtocolV2.minhash_functions import *

def create_dict_identificationNumber_name(df_standard):
    identificationNumber_name = {"Repetidos": []}
    
    # Itera pelas linhas do DataFrame
    for _, row in df_standard.iterrows():
        name = str(row["name"])
        short_name = str(row["short_name"])
        identification_number = str(row["identification_number"])
        
        if identification_number not in identificationNumber_name:
            identificationNumber_name[identification_number] = [name, short_name]
        
        else:
            identificationNumber_name["Repetidos"].append(identification_number)
        
    with open("Standard-identificationNumber_name.json", "w", encoding="utf-8") as f:
        json.dump(identificationNumber_name, f, ensure_ascii=False, indent=4)


def create_dict_name_identificationNumber(df_standard):
    name_identificationNumber = {}

    for _, row in df_standard.iterrows():
        name = str(row["name"])
        short_name = str(row["short_name"])
        identification_number = str(row["identification_number"])

        for key in [name, short_name]:
            if key not in name_identificationNumber:
                name_identificationNumber[key] = {identification_number}
            else:
                name_identificationNumber[key].add(identification_number)

    # Converter sets em listas para serializar com JSON
    name_identificationNumber = {k: list(v) for k, v in name_identificationNumber.items()}

    with open("Standard-name_identificationNumber.json", "w", encoding="utf-8") as f:
        json.dump(name_identificationNumber, f, ensure_ascii=False, indent=4)


def create_dict_words_names(df_standard):
    words_names = {}
    
    for _, row in df_standard.iterrows():
        name = str(row["name"])
        words = simplify_name(name).split()
        for word in words:
            if word not in words_names:
                words_names[word] = set()
            words_names[word].add(name)

    words_names = {k: list(v) for k, v in words_names.items()}
    
    with open("Standard-words_names.json", "w", encoding="utf-8") as f:
        json.dump(words_names, f, ensure_ascii=False, indent=4)


def create_unique_names_file(words_names_dict):
    with open("Standard-unique_words.txt", "w", encoding="utf-8") as f:
        for word in words_names_dict:
            if not word.isnumeric() and len(word) >= 3 and len(words_names_dict[word]) <= 7:
                f.write(f"{word}\n") 


def create_not_unique_names_file(words_names_dict):
    with open("Standard-unique_words.txt", "w", encoding="utf-8") as f:
        for word in words_names_dict:
            if not word.isnumeric()  and len(words_names_dict[word]) > 7:
                f.write(f"{word}\n") 


def read_unique_words_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        words = {line.strip().lower() for line in file if line.strip()}  # Remove duplicates and empty lines
    return words


def create_minHashLSH_table(df_standard):
    lsh = MinHashLSH(threshold=0.8, num_perm=128)   # Criar um índice LSH para encontrar nomes similares rapidamente 
    minhashes = {}  # Dicionário para armazenar MinHashes
    for _, row in df_standard.iterrows():
        standard_name = str(row["name"])
        standard_short_name = str(row["short_name"])
        if standard_name not in minhashes:
            minhashes[standard_name] = get_minhash(clean_name(standard_name))
            lsh.insert(standard_name, minhashes[standard_name])
        if standard_short_name not in minhashes:
            minhashes[standard_short_name] = get_minhash(clean_name(standard_short_name))
            lsh.insert(standard_short_name, minhashes[standard_short_name])
    
    with open("Standard-minhashlsh.pkl", "wb") as f:
        pickle.dump((lsh, minhashes), f)
