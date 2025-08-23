import pandas as pd
import os
import json 
import Levenshtein
import pickle
from datasketch import MinHash
import unicodedata
import re


translation_table = str.maketrans({
        ".": "",   # Remove dots
        "_": "",   # Remove underscores
        "-": " ",  # Replace hyphens with space
        ",": " ",   # Replace commas with space
        "\"": "",  # Remove double quotes
        "(": "",   # Remove opening parenthesis
        ")": "",    # Remove closing parenthesis
        "/": " "
    })


def read_unique_words_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        words = {line.strip().lower() for line in file if line.strip()}  # Remove duplicates and empty lines
    return words


def filter_best_match(row_name, names_list, unique_words):
    if len(names_list) == 0:
        return []
    
    simplified_row_name = remove_non_unique_words(simplify_name(row_name), unique_words)
    if simplified_row_name == "":
        return []
    
    current_best = names_list[0]
    limit_distance = (len(row_name) * 0.3)
    simplified_current_best = remove_non_unique_words(simplify_name(current_best), unique_words)
    best_distance = Levenshtein.distance(simplified_row_name, simplified_current_best)

    if len(names_list) == 1:
        if best_distance >= limit_distance:
            return []
        return current_best
    
    for possible_best in names_list[1:]:
        simplified_possible_best = remove_non_unique_words(simplify_name(possible_best), unique_words)
        current_distance = Levenshtein.distance(simplified_row_name, simplified_possible_best)
        if current_distance < best_distance:
            best_distance = current_distance
            current_best = possible_best
    
    if best_distance >= limit_distance:
        return []
    return current_best


def simplify_name(name):
    simplified_name = ""
    for char in name:
        if char == "´" or char == "`" or char == "’":
            simplified_name += ""
        else:
            simplified_name += char

    # Remove acentos e caracteres especiais
    simplified_name = unicodedata.normalize('NFKD', simplified_name).encode('ASCII', 'ignore').decode('ASCII')

    # Converte tudo para minúsculas
    simplified_name = simplified_name.lower()

    return simplified_name.translate(translation_table)


def clean_name(name):
    # Remove acentos e caracteres especiais
    name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
    
    # Converte tudo para minúsculas
    name = name.lower()
    
    # Remove todos os espaços
    name = name.replace(" ", "")
    
    # Remove caracteres especiais como "-", ";", ".", "_", etc.
    name = re.sub(r'[^a-z0-9]', '', name)
    
    return name


def remove_non_unique_words(name, unique_words):
    return " ".join(word for word in name.split() if word in unique_words)


def get_shingles(text, n=2):
    return [text[i:i+n] for i in range(len(text) - n + 1)]


def jaccard_similarity(m1, m2):
    return m1.jaccard(m2)


def get_minhash(text, num_perm=128):
    m = MinHash(num_perm=num_perm)
    for shingles in get_shingles(text):
        m.update(shingles.encode('utf8'))
    return m


with open("Standard-minhashlsh.pkl", "rb") as f:
    lsh, minhashes = pickle.load(f)


def main(testName):
    unique_words = read_unique_words_from_file("Standard-unique_words.txt")  


    print(f"Original Name: {testName}\n")

    
    clean_testName = clean_name(testName)
    print(f"Cleaned Name: {clean_testName}\n")

    
    possible_names = lsh.query(get_minhash(clean_testName))
    print("Possible Names:\n")
    for index, possible_name in enumerate(possible_names):
        print(f"{index+1} - <{possible_name}>")
    print("\n")

    
    if len(possible_names) == 0:
        return []
    
    
    simplified_testName = simplify_name(testName)
    print(f"Simplified original Name: {simplified_testName}\n")


    removed_uniqueWords_simplified_testName = remove_non_unique_words(simplified_testName, unique_words)
    print(f"Simplified original Name without unique words: {removed_uniqueWords_simplified_testName}\n")
    if removed_uniqueWords_simplified_testName == "":
        return []
    
    print("-"*90)

    current_best = possible_names[0]
    limit_distance = (len(removed_uniqueWords_simplified_testName) * 0.3)
    print(f"Limit Distace: {limit_distance}\n")
    
    simplified_current_best = simplify_name(current_best)
    print(f"Simplified current best Name: {simplified_current_best}\n")


    removed_uniqueWords_simplified_current_best = remove_non_unique_words(simplified_current_best, unique_words).strip()
    print(f"Simplified current best Name without unique words: {removed_uniqueWords_simplified_current_best}\n")
    
    
    best_distance = Levenshtein.distance(removed_uniqueWords_simplified_testName, removed_uniqueWords_simplified_current_best)
    print(f"Current Distace: {best_distance}")

    print("-"*90)

    if len(possible_names) == 1:
        print("RESULTS:\n")
        if best_distance >= limit_distance:
            print("No matches 1")
            return []
        print(f"Best Match (only one option): <{current_best}>")
        return current_best
    
    for possible_best in possible_names[1:]:
        simplified_possible_best = simplify_name(possible_best)
        print(f"Simplified possible best Name: {simplified_possible_best}\n")

        removed_uniqueWords_simplified_possible_best = remove_non_unique_words(simplified_possible_best, unique_words)
        print(f"Simplified possible best Name without unique words: {removed_uniqueWords_simplified_possible_best}\n")

        current_distance = Levenshtein.distance(removed_uniqueWords_simplified_possible_best, simplified_possible_best)
        print(f"Current Distace: {current_distance}")

        print("-"*90)

        if current_distance < best_distance:
            best_distance = current_distance
            current_best = possible_best
    
    print("RESULTS:\n")
    if best_distance >= limit_distance:
        print("No matches 2")
        return []
    print(f"Best Match: <{current_best}>")
    return current_best



print("-"*90)
print("\tTESTE 1")
testeName = "HAND LINE TRANSPORTES INTERNACIONAIS LTDA"
print("-"*90)
print("\n")
main(testeName)


print("\n")
print("\n")
print("-"*90)
print("\tTESTE 2")
testeName = "EDUARDO RANGEL DESPACHANTE OFICIAL, LDA." 
print("-"*90)
print("\n")
main(testeName)


print("\n")
print("\n")
print("-"*90)
print("\tTESTE 3")
testeName = "PSA SINES" 
print("-"*90)
print("\n")
main(testeName)


print("\n")
print("\n")
print("-"*90)
print("\tTESTE 4")
testeName = "KUEHNE   NAGEL INC" 
print("-"*90)
print("\n")
main(testeName)