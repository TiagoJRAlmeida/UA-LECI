import pandas as pd
import os
import json 
import Levenshtein
import re
from itertools import combinations
import unicodedata


def find_possible_match(row_name, lists):
    row_name = row_name.lower()
    limit_distance = (len(row_name) * 0.2)
    current_best_match = [None, 0]
    for current_list in lists:
        for name in current_list:
            current_distance = Levenshtein.distance(row_name, name.lower()) 
            if current_distance <= limit_distance and (current_distance < current_best_match[1] or current_best_match[1] == 0):
                current_best_match = [name, current_distance]

    return current_best_match[0] 


def get_best_result(row_name, lists):
    if len(lists) == 0:
        return []
    
    limit_distance = (len(row_name) * 0.9)
    current_best = lists[0]
    current_best_distance = Levenshtein.distance(row_name, current_best)

    if len(lists) == 1:
        if current_best_distance >= limit_distance:
            return []
        return lists[0]
    
    for possible_best in lists[1:]:
        current_distance = Levenshtein.distance(row_name, possible_best)
        if current_distance < current_best_distance:
            current_best_distance = current_distance
            current_best = possible_best
    
    if current_best_distance >= limit_distance:
        return []
    return current_best


def get_unique_words_lists(word_dict, name):
    words = name.split()
    return [word_dict[word] for word in words if word in word_dict and len(word_dict[word]) < 20]


def max_intersection(lists):
    max_result = set()
    best_sequence = []
    
    # Gerar todas as combinações possíveis de interseção
    for r in range(2, len(lists) + 1):
        for combo in combinations(lists, r):
            intersection_result = set(combo[0])
            sequence = [combo[0]]
            
            for lst in combo[1:]:
                intersection_result &= set(lst)
                sequence.append(lst)
                
                # Atualiza a melhor interseção encontrada
                if len(intersection_result) > len(max_result):
                    max_result = intersection_result
                    best_sequence = sequence[:]
    
    # Se nenhuma interseção foi encontrada, retorna a menor lista
    if not max_result:
        min_list = min(lists, key=len) if lists else []
        return [min_list], set(min_list)
    
    return best_sequence, max_result


def remove_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def clean_row_name(s):
    s = remove_accents(s)  # Remove accents (ç -> c, ã -> a, etc.)
    s = re.sub(r'[^a-zA-Z0-9]', ' ', s)  # Replace special characters with spaces
    return re.sub(r'\s+', ' ', s).strip().lower()  # Remove extra spaces and lowercase


def read_unique_words_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        words = {line.strip().lower() for line in file if line.strip()}  # Remove duplicates and empty lines
    return sorted(words)


# Steps to Implement:
# 1. Split the cleaned name into words.
# 2. Check if any of the words exist in unique_words.
#       --> If a part of a word matches a unique word, separate it.
# 3. Check if merging words results in a match with unique_words.
#       --> Iterate through combinations to find valid merges.
def reformat_row_name(unique_words, s):
    words = s.split()  # Split cleaned row name into words (1)
    new_words = []

    # Check if any part of a word matches a unique word (2)
    for word in words:
        if word in unique_words: # If word already is unique, we wont look for uniques inside it
            new_words.append(word)
        else:
            temp = word
            separated = []
            while temp:
                for u_word in unique_words:
                    if temp.startswith(u_word):
                        separated.append(u_word)
                        temp = temp[len(u_word):]
                        break
                else:
                    separated.append(temp)
                    break
            new_words.extend(separated)

    # Try merging words to form unique words
    final_words = []
    skip = 0
    for i, word in enumerate(new_words):
        if skip:
            skip -= 1
            continue
        
        merged = word
        for j in range(i+1, len(new_words)):
            merged += new_words[j]
            if merged in unique_words:
                final_words.append(merged)
                skip = j - i  # Skip these words in next iteration
                break
        else:
            final_words.append(word)

    return " ".join(final_words)


def find_standard_name(row_name, unique_words, words_names):
    cleaned_row_name = clean_row_name(row_name)
    reformated_cleaned_row_name = reformat_row_name(unique_words, cleaned_row_name)
    unique_words_lists = get_unique_words_lists(words_names, reformated_cleaned_row_name)
    possible_result = find_possible_match(row_name, unique_words_lists)
    if possible_result != None:
        return possible_result
    return get_best_result(row_name, list(max_intersection(unique_words_lists)[1]))


def create_file_unique_words(words_names, prefix):
    with open(f"{prefix}-unique_words.txt", "w", encoding="utf-8") as f:
        for word in words_names:
            if not word.isnumeric() and len(word) >= 4 and len(words_names[word]) <= 10:
                f.write(f"{word}\n") 


def get_unique_words_lists(word_dict, name):
    words = clean_string(name).split()
    return [word_dict[word] for word in words if word in word_dict and len(word_dict[word]) < 20]


def max_intersection(lists):
    max_result = set()
    best_sequence = []
    
    # Gerar todas as combinações possíveis de interseção
    for r in range(2, len(lists) + 1):
        for combo in combinations(lists, r):
            intersection_result = set(combo[0])
            sequence = [combo[0]]
            
            for lst in combo[1:]:
                intersection_result &= set(lst)
                sequence.append(lst)
                
                # Atualiza a melhor interseção encontrada
                if len(intersection_result) > len(max_result):
                    max_result = intersection_result
                    best_sequence = sequence[:]
    
    # Se nenhuma interseção foi encontrada, retorna a menor lista
    if not max_result:
        min_list = min(lists, key=len) if lists else []
        return [min_list], set(min_list)
    
    return best_sequence, max_result


def intersect_name_lists(word_dict, name):
    words = clean_string(name).split()
    result_sets = [set(word_dict[word]) for word in words if word in word_dict]
    
    if not result_sets:
        return []
    
    return list(set.intersection(*result_sets))


def create_dict_words_names(df_standard, prefix):
    words_names = {}
    
    for _, row in df_standard.iterrows():
        name = str(row["name"])
        words = clean_string(name).split()
        for word in words:
            if word not in words_names:
                words_names[word] = set()
            words_names[word].add(name)

        # short_name = str(row["short_name"])
        # words = clean_string(short_name).split()
        # for word in words:
        #     if word not in words_names:
        #         words_names[word] = set()
        #     words_names[word].add(name)

    words_names = {k: list(v) for k, v in words_names.items()}
    
    with open(f"{prefix}-words_names.json", "w", encoding="utf-8") as f:
        json.dump(words_names, f, ensure_ascii=False, indent=4)
    
    
def create_dict_namesSynonyms(df_standard, prefix):
    namesSynonyms = {}
    
    for _, row in df_standard.iterrows():
        name = str(row["name"])
        
        if name not in namesSynonyms:
            namesSynonyms[name] = True
            
    with open(f"{prefix}-namesSynonyms.json", "w", encoding="utf-8") as f:
        json.dump(namesSynonyms, f, ensure_ascii=False, indent=4)
        
        
def create_dict_identificationNumber_name(df_standard, prefix):
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
        
    with open(f"{prefix}-identificationNumber_name.json", "w", encoding="utf-8") as f:
        json.dump(identificationNumber_name, f, ensure_ascii=False, indent=4)
            

def remove_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def clean_string(s):
    s = remove_accents(s)  # Remove accents (ç -> c, ã -> a, etc.)
    return re.sub(r'[^a-zA-Z0-9 ]', '', s).lower()


def main(test_table):
    
    if test_table != "departure" and test_table != "transport":
        print("Opções de teste:\n1) departure\n2) transport")
        return
        
    corrigido = 0
    nao_corrigido = 0
    ja_corrigido = 0
    sem_identification_number = 0
    current_row = 0
    identification_number_repetido_skipped = 0
    prefix = None
    apagar = {}
    wrongNamesCount = {}

    if test_table == "departure":
        prefix = "Departure"
        # Lê o CSV com uso eficiente da memória
        print("\nA ler Tabela de Departure")
        df = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Departure_Document_Data.csv', sep=';', low_memory=False)
        print("Tabela de Departure lida!")
        print(f"Numero de linhas da tabela Departure: {len(df)}\n")
        
    else:
        prefix = "Transport"
        # Lê o CSV com uso eficiente da memória
        print("\nA ler Tabela de Transport")
        df = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Transport_Document_Data.csv', sep=';', low_memory=False)
        print("Tabela de Transport lida!")
        print(f"Numero de linhas da tabela Transport: {len(df)}\n")


    # Lê o CSV com uso eficiente da memória
    if not os.path.isfile(f"{prefix}-identificationNumber_name.json") or not os.path.isfile(f"{prefix}-namesSynonyms.json"): 
        print("A ler Tabela de agentes standardizados")
        df_standard = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Tabela_de_Agentes_Standardizados.csv', sep=';', low_memory=False)
        print("Tabela de agentes standardizados lida!")
        
        if not os.path.isfile(f"{prefix}-identificationNumber_name.json"):
            print("\n--- A criar Dicionário identificationNumber_name ---")
            create_dict_identificationNumber_name(df_standard, prefix)
            print("--- Dicionário identificationNumber_name criado e guardado em identificationNumber_name.json! ---")
            
        if not os.path.isfile(f"{prefix}-namesSynonyms.json"):
            print("\n--- A criar Dicionário namesSynonyms ---")
            create_dict_namesSynonyms(df_standard, prefix)
            print("--- Dicionário namesSynonyms criado e guardado em namesSynonyms.json! ---")
            
        if not os.path.isfile(f"{prefix}-words_names.json"):
            print("\n--- A criar Dicionário words_names ---")
            create_dict_words_names(df_standard, prefix)
            print("--- Dicionário words_names criado e guardado em words_names.json! ---")


    # Abrir o dicionário identificationNumber_name.json
    with open(f'{prefix}-identificationNumber_name.json', 'r', encoding="utf-8") as file:
        identificationNumber_name = json.load(file)
        
    # Abrir o dicionário namesSynonyms.json
    with open(f'{prefix}-namesSynonyms.json', 'r', encoding="utf-8") as file:
        namesSynonyms = json.load(file)
            
    # Abrir o dicionário words_names.json
    with open(f'{prefix}-words_names.json', 'r', encoding="utf-8") as file:
        words_names = json.load(file)

    if not os.path.isfile(f"{prefix}-unique_words.txt"):
            print("\n--- A criar o ficheiro unique_words ---")
            create_file_unique_words(words_names, prefix)
            print("--- Ficheiro unique_words criado e guardado em unique_words.txt! ---")

    # Abrir a lista de nomes unicos unique_names.txt
    unique_words_list = read_unique_words_from_file(f'{prefix}-unique_words.txt')    

    # Abrir o dicionário wrongNames.json
    if os.path.isfile(f"{prefix}-wrongNames.json"):
        with open(f'{prefix}-wrongNames.json', 'r', encoding="utf-8") as file:
            wrongNames = json.load(file)
    else:
        wrongNames = {}

        
    # Itera pelas linhas do DataFrame
    for _, row in df.iterrows():
        row_name = str(row["name"])
        identification_number = str(row["identification_number"])
        
        if identification_number in identificationNumber_name["Repetidos"]:
            identification_number_repetido_skipped += 1
            if row_name not in wrongNamesCount:
                wrongNamesCount[row_name] = 0
            wrongNamesCount[row_name] += 1
            continue
        

        if identification_number in identificationNumber_name:
            standard_name = identificationNumber_name[identification_number][0]
            standard_short_name = identificationNumber_name[identification_number][1]
            if row_name == standard_name or row_name == standard_short_name:
                ja_corrigido += 1
            
            else:
                cleaned_row_name = clean_string(row_name)
                cleaned_standard_name = clean_string(standard_name)
                cleaned_standard_short_name = clean_string(standard_short_name)

                name_distance = Levenshtein.distance(cleaned_row_name, cleaned_standard_name)
                short_name_distance = Levenshtein.distance(cleaned_row_name, cleaned_standard_short_name)
                limit_distance = (len(row_name) * 0.9)
                if name_distance > limit_distance and short_name_distance > limit_distance:
                    
                    if identification_number not in wrongNames:
                        wrongNames[identification_number] = {
                            "Correct_Name": [],
                            "Wrong_Name": []
                        }

                    if standard_name not in wrongNames[identification_number]["Correct_Name"]:
                        wrongNames[identification_number]["Correct_Name"].append(standard_name)

                    if row_name not in wrongNames[identification_number]["Wrong_Name"]:
                        wrongNames[identification_number]["Wrong_Name"].append(row_name)

                    if row_name not in wrongNamesCount:
                        wrongNamesCount[row_name] = 0
                    wrongNamesCount[row_name] += 1

                    if row_name not in apagar:
                        possible_name = find_standard_name(row_name, unique_words_list, words_names)
                        if possible_name == standard_name or possible_name == standard_short_name:
                            corrigido += 1
                            apagar[row_name] = {
                                "Identification_number": identification_number,
                                "Identification_number in Standard": True,
                                "Correct": True,
                                "possible_names": possible_name
                            }
                        else:
                            nao_corrigido += 1
                            apagar[row_name] = {
                                "Identification_number": identification_number,
                                "Identification_number in Standard": True,
                                "Correct": False,
                                "possible_names": possible_name
                            }        
                else:
                    corrigido += 1
                    
                    if row_name not in namesSynonyms:
                        namesSynonyms[row_name] = standard_name


        else:
            if row_name in namesSynonyms:
                if namesSynonyms[row_name] == True:
                    ja_corrigido += 1
                    
                else:
                    corrigido += 1
                    
            else:
                nao_corrigido += 1
                if row_name not in apagar:
                    possible_name = find_standard_name(row_name, unique_words_list, words_names)
                    apagar[row_name] = {
                        "Identification_number": identification_number,
                        "Identification_number in Standard": False,
                        "Correct": False,
                        "possible_names": possible_name
                    }

                if row_name not in wrongNamesCount:
                    wrongNamesCount[row_name] = 0
                wrongNamesCount[row_name] += 1
                
        print(f"\rCurrent Row: {current_row}", end="")
        current_row += 1
        
        
    with open(f"{prefix}-namesSynonyms.json", "w", encoding="utf-8") as f:
        json.dump(namesSynonyms, f, ensure_ascii=False, indent=4)
        
    with open(f"{prefix}-wrongNames.json", "w", encoding="utf-8") as f:
        json.dump(wrongNames, f, ensure_ascii=False, indent=4)
        
    with open(f"{prefix}-identificationNumber_name.json", "w", encoding="utf-8") as f:
        json.dump(identificationNumber_name, f, ensure_ascii=False, indent=4)

    # Ordenar wrongNamesCount pelo valor (número de ocorrências) em ordem decrescente
    sorted_wrongNamesCount = dict(sorted(wrongNamesCount.items(), key=lambda item: item[1], reverse=True))
    with open(f"{prefix}-wrongNames_Count.json", "w", encoding="utf-8") as f:
        json.dump(sorted_wrongNamesCount, f, ensure_ascii=False, indent=4)

    # Ordena "apagar" com base na ordem das chaves em "wrongNamesCount"
    sorted_apagar = {key: apagar[key] for key in sorted_wrongNamesCount if key in apagar}
    with open(f"{prefix}-apagar.json", "w", encoding="utf-8") as f:
        json.dump(sorted_apagar, f, ensure_ascii=False, indent=4)
        
        
    print(f"""\nEstatisticas:
        Corrigidos = {corrigido}
        Não Corrigido = {nao_corrigido}
        Já Corrigido = {ja_corrigido}
        Sem Identification_Number = {sem_identification_number} 
        Identification_Number Repetido --> Skipped = {identification_number_repetido_skipped}
        Percentagem de nomes corrigidos = {((corrigido + ja_corrigido) / len(df))*100:.3f}%
          """)
    

print("\n")
print("-"*90)   
print("\nA começar os testes da tabela TRANSPORT")
main("transport")
print("\n")
print("-"*90)
print("\nA começar os testes da tabela DEPARTURE")
main("departure")
print("\n")
print("-"*90) 