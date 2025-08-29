import pandas as pd
import os
import json 
import Levenshtein
import time
from table_functions import *
from minhash_functions import *
from file_manipulation import *
# from strings_manipulation import *
import sqlite3
    

start_time = time.time()


def filter_best_match(row_name, names_list, unique_words):
    if len(names_list) == 0:
        return []
    
    simplified_row_name = remove_non_unique_words(simplify_name(row_name), unique_words)
    if simplified_row_name == "":
        return []
    
    current_best = names_list[0]
    limit_distance = (len(simplified_row_name) * 0.3)
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


def main(test_table):
    if test_table != "departure" and test_table != "transport":
        print("Opções de teste:\n1) departure\n2) transport")
        return
        
    already_corrected_count = 0
    name_corrected_count = 0
    name_and_identificationNumber_corrected_count = 0
    not_corrected_count = 0
    no_identification_number_count = 0
    repeated_identificationNumber_skipped_count = 0
    corrected_by_synonym_count = 0

    current_row = 0
    table = None

    best_matches_corrected = {}
    best_match_not_found = {}
    wrongNamesCount = {}    
    synonyms = {}

    non_standard_names = set()


    # Criar um dataframe para guardar alterações para efeito de estatisticas
    corrections = {
        "Table": [],
        "Original Name": [],
        "Identification Number": [],
        "Chossen Standard Name": [],
        "Standard Identification Number": [],
        "Cleaned Original Name": [],
        "Cleaned Standard Name": [],
        "Method Used": []
    }

    # Ler a tabela standard    
    df_standard = read_standard_table()

    if not os.path.exists("Standard-minhashlsh.pkl"):
        print("\n--- A criar MinHashLSH ---")
        create_minHashLSH_table(df_standard)
        print("--- MinHashLSH Criado e guardado no ficheiro minhashlsh.pkl! ---")
    with open("Standard-minhashlsh.pkl", "rb") as f:
        lsh, minhashes = pickle.load(f)

    if test_table == "departure":
        table = "Departure"
        df = read_departure_table()
    else:
        table = "Transport"
        df = read_transport_table()


    if not os.path.isfile("Standard-words_names.json"):
        print("\n--- A criar Dicionário words_names ---")
        create_dict_words_names(df_standard)
        print("--- Dicionário words_names criado e guardado em Standard-words_names.json! ---")
    with open('Standard-words_names.json', 'r', encoding="utf-8") as file:
        words_names = json.load(file)


    if not os.path.isfile("Standard-unique_words.txt"):
        print("\n--- A criar o ficheiro unique_words ---")
        create_unique_names_file(words_names)
        print("--- Ficheiro unique_words criado e guardado em Standard-unique_words.txt! ---")
    unique_words = read_unique_words_from_file("Standard-unique_words.txt")    
        

    if not os.path.isfile("Standard-identificationNumber_name.json"):
        print("\n--- A criar Dicionário identificationNumber_name ---")
        create_dict_identificationNumber_name(df_standard)
        print("--- Dicionário identificationNumber_name criado e guardado em Standard-identificationNumber_name.json! ---")
    with open('Standard-identificationNumber_name.json', 'r', encoding="utf-8") as file:
        identificationNumber_name = json.load(file)


    if not os.path.isfile("Standard-name_identificationNumber.json"):
        print("\n--- A criar Dicionário name_identificationNumber ---")
        create_dict_name_identificationNumber(df_standard)
        print("--- Dicionário name_identificationNumber criado e guardado em Standard-name_identificationNumber.json! ---")
    with open('Standard-name_identificationNumber.json', 'r', encoding="utf-8") as file:
        name_identificationNumber = json.load(file)
    

    # Itera pelas linhas do Dataset (Transport ou Departure)
    print("\n")
    for _, row in df.iterrows():
        row_name = str(row["name"])
        identification_number = str(row["identification_number"])

        print(f"\rCurrent Row: {current_row}", end="")
        current_row += 1

        ## Para os casos onde a linha tem o identification number e está no standard mas é repetido
        if identification_number in identificationNumber_name["Repetidos"]:
            repeated_identificationNumber_skipped_count += 1
            if f"{row_name} | {str(identification_number)} | {identificationNumber_name[identification_number][0]} | {identificationNumber_name[identification_number][1]}" not in wrongNamesCount:
                wrongNamesCount[f"{row_name} | {str(identification_number)} | {identificationNumber_name[identification_number][0]} | {identificationNumber_name[identification_number][1]}"] = 1
            else:
                wrongNamesCount[f"{row_name} | {str(identification_number)} | {identificationNumber_name[identification_number][0]} | {identificationNumber_name[identification_number][1]}"] += 1
            corrections["Table"].append(table)
            corrections["Original Name"].append(row_name)
            corrections["Identification Number"].append(identification_number)
            corrections["Chossen Standard Name"].append("Null")
            corrections["Standard Identification Number"].append("Null")
            corrections["Cleaned Original Name"].append(clean_name(row_name))
            corrections["Cleaned Standard Name"].append("Null")
            corrections["Method Used"].append("Standard Identification Number Repeated")
            continue
        

        ## Para os casos onde a linha tem o identification number e está no standard
        if identification_number in identificationNumber_name:
            standard_name = identificationNumber_name[identification_number][0]
            standard_short_name = identificationNumber_name[identification_number][1]
            cleaned_row_name = clean_name(row_name)
            cleaned_standard_name = clean_name(standard_name)
            cleaned_standard_short_name = clean_name(standard_short_name)

            ### Caso o row name seja igual ao standard name associado ao identification number
            if row_name == standard_name or row_name == standard_short_name or\
            cleaned_row_name in cleaned_standard_name or\
            cleaned_row_name in cleaned_standard_short_name:
                #### Adiciona ao dicionário de sinonimos e ao df de correções
                corrections["Table"].append(table)
                corrections["Original Name"].append(row_name)
                corrections["Identification Number"].append(identification_number)
                corrections["Standard Identification Number"].append(identification_number)
                corrections["Cleaned Original Name"].append(clean_name(row_name))
                corrections["Method Used"].append("Already Correct")
                if row_name == standard_name:
                    synonyms[row_name] = [standard_name, identification_number]
                    corrections["Chossen Standard Name"].append(standard_name)
                    corrections["Cleaned Standard Name"].append(clean_name(standard_name))
                else:
                    synonyms[row_name] = [standard_short_name, identification_number]
                    corrections["Chossen Standard Name"].append(standard_short_name)
                    corrections["Cleaned Standard Name"].append(clean_name(standard_short_name))
                already_corrected_count += 1
                continue
            

            ### Caso o row name seja parecido o suficiente ao standard name associado ao identification number (a partir da distancia de levenshtein)
            limit_distance = len(cleaned_row_name) * 0.3 # Melhor valor testado
            distance_to_standard_name = Levenshtein.distance(cleaned_row_name, cleaned_standard_name) 
            distance_to_standard_short_name = Levenshtein.distance(cleaned_row_name, cleaned_standard_short_name)

            if  distance_to_standard_name <= limit_distance or distance_to_standard_short_name <= limit_distance:

                #### Adiciona ao dicionário de sinonimos e ao df de correções
                corrections["Table"].append(table)
                corrections["Original Name"].append(row_name)
                corrections["Identification Number"].append(identification_number)
                corrections["Standard Identification Number"].append(identification_number)
                corrections["Cleaned Original Name"].append(clean_name(row_name))
                corrections["Method Used"].append("Levenshtein Distance")
                if distance_to_standard_name < distance_to_standard_short_name:
                    synonyms[row_name] = [standard_name, identification_number]
                    corrections["Chossen Standard Name"].append(standard_name)
                    corrections["Cleaned Standard Name"].append(clean_name(standard_name))
                else:
                    synonyms[row_name] = [standard_short_name, identification_number]
                    corrections["Chossen Standard Name"].append(standard_short_name)
                    corrections["Cleaned Standard Name"].append(clean_name(standard_short_name))
                name_corrected_count += 1
                continue

            ### Caso o row name NÃO seja parecido o suficiente ao standard name associado ao identification number (a partir da distancia de levenshtein)
            ### Usa-se o dicionário de sinonimos para encontrar uma match ou, caso não exista uma correspondencia, o MinHash.
            else:
                
                #### Para os casos onde a linha tem o nome no dicionario de sinonimos
                if row_name in synonyms:
                    corrections["Table"].append(table)
                    corrections["Original Name"].append(row_name)
                    corrections["Identification Number"].append(identification_number)
                    corrections["Chossen Standard Name"].append(synonyms[row_name][0])
                    corrections["Standard Identification Number"].append(synonyms[row_name][1])
                    corrections["Cleaned Original Name"].append(clean_name(row_name))
                    corrections["Cleaned Standard Name"].append(clean_name(synonyms[row_name][0]))
                    corrections["Method Used"].append("Synonyms Table")
                    corrected_by_synonym_count += 1
                    continue
                
                #### Ver as possiveis opções através de MinHash    
                possible_names = lsh.query(get_minhash(clean_name(row_name)))
                best_match = filter_best_match(row_name, possible_names, unique_words)
                
                #### Se NÃO foi encontrada nenhuma opção que seja boa o suficiente, o nome provavelmente não está no standard (adicionar ao set)
                if not best_match:
                    if f"{row_name} | {str(identification_number)} | {identificationNumber_name[identification_number][0]} | {identificationNumber_name[identification_number][1]}" not in wrongNamesCount:
                        wrongNamesCount[f"{row_name} | {str(identification_number)} | {identificationNumber_name[identification_number][0]} | {identificationNumber_name[identification_number][1]}"] = 1
                    else:
                        wrongNamesCount[f"{row_name} | {str(identification_number)} | {identificationNumber_name[identification_number][0]} | {identificationNumber_name[identification_number][1]}"] += 1
                    if row_name not in best_match_not_found:
                        best_match_not_found[row_name] = {
                            "Identification_number": identification_number,
                            "Standard Name": standard_name,
                            "possible_names": possible_names
                        }
                    non_standard_names.add(row_name)
                    not_corrected_count += 1
                    continue
                
                #### Se foi encontrado uma opção boa o suficiente, ver se é preciso corrigir tambem o identification number
                else: 
                    if row_name not in best_matches_corrected:
                        best_matches_corrected[row_name] = {
                            "Identification_number": identification_number,
                            "Standard Name": standard_name,
                            "possible_names": possible_names,
                            "best match": best_match
                        } 

                    ##### Se a melhor opção encontrada for igual ao standard name associado ao identification number, apenas é preciso corrigir o nome da linha
                    if best_match == standard_name or best_match == standard_short_name:

                        ###### Adiciona ao dicionário de sinonimos e ao df de correções
                        corrections["Table"].append(table)
                        corrections["Original Name"].append(row_name)
                        corrections["Identification Number"].append(identification_number)
                        corrections["Cleaned Original Name"].append(clean_name(row_name))
                        corrections["Method Used"].append("MinHash Best Match")
                        if best_match == standard_name:
                            synonyms[row_name] = [standard_name, identification_number]
                            corrections["Chossen Standard Name"].append(standard_name)
                            corrections["Standard Identification Number"].append(name_identificationNumber[standard_name][0])
                            corrections["Cleaned Standard Name"].append(clean_name(standard_name))
                        else:
                            synonyms[row_name] = [standard_short_name, identification_number]
                            corrections["Chossen Standard Name"].append(standard_short_name)
                            corrections["Standard Identification Number"].append(name_identificationNumber[standard_short_name][0])
                            corrections["Cleaned Standard Name"].append(clean_name(standard_short_name))
                        name_corrected_count += 1
                        continue 
                    
                    ##### Caso contrário, tambem se corrige o identification number
                    else:
                        ###### Adiciona ao dicionário de sinonimos e ao df de correções
                        synonyms[row_name] = [best_match, name_identificationNumber[best_match][0]]
                        corrections["Table"].append(table)
                        corrections["Original Name"].append(row_name)
                        corrections["Identification Number"].append(identification_number)
                        corrections["Chossen Standard Name"].append(best_match)
                        corrections["Standard Identification Number"].append(name_identificationNumber[best_match][0])
                        corrections["Cleaned Original Name"].append(clean_name(row_name))
                        corrections["Cleaned Standard Name"].append(clean_name(best_match))
                        corrections["Method Used"].append("MinHash Best Match")
                        name_and_identificationNumber_corrected_count += 1
                        continue 



        # Para os casos onde a linha ou tem identification number e não está no standard, ou simplemente não tem identification number
        else:

            ## Se a linha não tem identification number, usa-se o dicionário de sinonimos para encontrar uma match ou, caso não exista uma correspondencia, o MinHash.
            if identification_number == "nan":

                ### Verificar se está no dicionário de sinonimos
                if row_name in synonyms:
                    corrections["Table"].append(table)
                    corrections["Original Name"].append(row_name)
                    corrections["Identification Number"].append("Null")
                    corrections["Chossen Standard Name"].append(synonyms[row_name][0])
                    corrections["Standard Identification Number"].append(synonyms[row_name][1])
                    corrections["Cleaned Original Name"].append(clean_name(row_name))
                    corrections["Cleaned Standard Name"].append(clean_name(synonyms[row_name][0]))
                    corrections["Method Used"].append("Synonyms Table")
                    corrected_by_synonym_count += 1
                    continue

                ### Ver as possiveis opções através de MinHash  
                possible_names = lsh.query(get_minhash(clean_name(row_name)))
                best_match = filter_best_match(row_name, possible_names, unique_words)

                ### Se NÃO foi encontrada nenhuma opção que seja boa o suficiente, o nome provavelmente não está no standard (adicionar ao set)
                if not best_match:
                    if f"{row_name} | Null | Null | Null" not in wrongNamesCount:
                        wrongNamesCount[f"{row_name} | Null | Null | Null"] = 1
                    else:
                        wrongNamesCount[f"{row_name} | Null | Null | Null"] += 1
                    if row_name not in best_match_not_found:
                        best_match_not_found[row_name] = {
                            "Identification_number": [],
                            "possible_names": possible_names
                        }
                    not_corrected_count += 1
                    corrections["Table"].append(table)
                    corrections["Original Name"].append(row_name)
                    corrections["Identification Number"].append("Null")
                    corrections["Chossen Standard Name"].append("Null")
                    corrections["Standard Identification Number"].append("Null")
                    corrections["Cleaned Original Name"].append(clean_name(row_name))
                    corrections["Cleaned Standard Name"].append("Null")
                    corrections["Method Used"].append("Not in Standard")
                    continue

                ### Se foi encontrado uma opção boa o suficiente, corrigir o nome e o identification number
                else:
                    ##### Adiciona ao dicionário de sinonimos e ao df de correções
                    synonyms[row_name] = [best_match, name_identificationNumber[best_match][0]]
                    corrections["Table"].append(table)
                    corrections["Original Name"].append(row_name)
                    corrections["Identification Number"].append("Null")
                    corrections["Chossen Standard Name"].append(best_match)
                    corrections["Standard Identification Number"].append(name_identificationNumber[best_match][0])
                    corrections["Cleaned Original Name"].append(clean_name(row_name))
                    corrections["Cleaned Standard Name"].append(clean_name(best_match))
                    corrections["Method Used"].append("MinHash Best Match")
                    name_and_identificationNumber_corrected_count += 1
                    continue 

            ## Se a linha tem identification number, mas não está no standard, usa-se o dicionário de sinonimos para encontrar uma match ou, caso não exista uma correspondencia, o MinHash.
            else:

                ### Se já se sabe que o nome é não standard, não se corrige por agora
                if row_name in non_standard_names:
                    not_corrected_count += 1
                    if f"{row_name} | {str(identification_number)} | Null | Null" not in wrongNamesCount:
                        wrongNamesCount[f"{row_name} | {str(identification_number)} | Null | Null"] = 1
                    else:
                        wrongNamesCount[f"{row_name} | {str(identification_number)} | Null | Null"] += 1
                    if row_name not in best_match_not_found:
                        best_match_not_found[row_name] = {
                            "Identification_number": identification_number,
                            "possible_names": possible_names
                        }
                    corrections["Table"].append(table)
                    corrections["Original Name"].append(row_name)
                    corrections["Identification Number"].append(identification_number)
                    corrections["Chossen Standard Name"].append("Null")
                    corrections["Standard Identification Number"].append("Null")
                    corrections["Cleaned Original Name"].append(clean_name(row_name))
                    corrections["Cleaned Standard Name"].append("Null")
                    corrections["Method Used"].append("Has NIF, But Not in Standard")
                    continue

                ### Caso contrário, verifica-se primeiro se está nos sinonimos e, se não encontrar, no minHash. Caso não se encontre uma match adiciona-se ao set dos não standard
                else:

                    #### Verificar se está no dicionário de sinonimos
                    if row_name in synonyms:
                        corrections["Table"].append(table)
                        corrections["Original Name"].append(row_name)
                        corrections["Identification Number"].append(identification_number)
                        corrections["Chossen Standard Name"].append(synonyms[row_name][0])
                        corrections["Standard Identification Number"].append(synonyms[row_name][1])
                        corrections["Cleaned Original Name"].append(clean_name(row_name))
                        corrections["Cleaned Standard Name"].append(clean_name(synonyms[row_name][0]))
                        corrections["Method Used"].append("Synonyms Table")
                        corrected_by_synonym_count += 1
                        continue

                    #### Ver as possiveis opções através de MinHash 
                    possible_names = lsh.query(get_minhash(clean_name(row_name)))
                    best_match = filter_best_match(row_name, possible_names, unique_words)

                    #### Se NÃO foi encontrada nenhuma opção que seja boa o suficiente, o nome provavelmente não está no standard (adicionar ao set)
                    if not best_match:
                        not_corrected_count += 1
                        if f"{row_name} | {str(identification_number)} | Null | Null" not in wrongNamesCount:
                            wrongNamesCount[f"{row_name} | {str(identification_number)} | Null | Null"] = 1
                        else:
                            wrongNamesCount[f"{row_name} | {str(identification_number)} | Null | Null"] += 1
                        if row_name not in best_match_not_found:
                            best_match_not_found[row_name] = {
                                "Identification_number": [],
                                "possible_names": possible_names
                            }
                        non_standard_names.add(row_name)
                        corrections["Table"].append(table)
                        corrections["Original Name"].append(row_name)
                        corrections["Identification Number"].append(identification_number)
                        corrections["Chossen Standard Name"].append("Null")
                        corrections["Standard Identification Number"].append("Null")
                        corrections["Cleaned Original Name"].append(clean_name(row_name))
                        corrections["Cleaned Standard Name"].append("Null")
                        corrections["Method Used"].append("Has NIF, But Not in Standard")
                        continue

                    #### Se foi encontrado uma opção boa o suficiente, corrigir o nome e o identification number
                    else:
                        if row_name not in best_matches_corrected:
                            best_matches_corrected[row_name] = {
                                "Identification_number": [],
                                "possible_names": possible_names,
                                "best match": best_match
                            } 

                        ###### Adiciona ao dicionário de sinonimos e ao df de correções
                        synonyms[row_name] = [best_match, name_identificationNumber[best_match][0]]
                        corrections["Table"].append(table)
                        corrections["Original Name"].append(row_name)
                        corrections["Identification Number"].append(identification_number)
                        corrections["Chossen Standard Name"].append(best_match)
                        corrections["Standard Identification Number"].append(name_identificationNumber[best_match][0])
                        corrections["Cleaned Original Name"].append(clean_name(row_name))
                        corrections["Cleaned Standard Name"].append(clean_name(best_match))
                        corrections["Method Used"].append("MinHash Best Match")
                        name_and_identificationNumber_corrected_count += 1
                        continue 
        

    with open(f"{table}-best_matches_corrected.json", "w", encoding="utf-8") as f:
        json.dump(best_matches_corrected, f, ensure_ascii=False, indent=4)
        
    # Ordenar wrongNamesCount pelo valor (número de ocorrências) em ordem decrescente
    sorted_wrongNamesCount = dict(sorted(wrongNamesCount.items(), key=lambda item: item[1], reverse=True))
    with open(f"{table}-wrongNamesCount.json", "w", encoding="utf-8") as f:
        json.dump(sorted_wrongNamesCount, f, ensure_ascii=False, indent=4)

    sorted_best_match_not_found = {key: best_match_not_found[key] for key in sorted_wrongNamesCount if key in best_match_not_found}
    with open(f"{table}-best_match_not_found.json", "w", encoding="utf-8") as f:
        json.dump(sorted_best_match_not_found, f, ensure_ascii=False, indent=4)

    # Conectar com a base de dados
    db_name = "analysis.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


    notCorrected = {
        "Name": [],
        "Identification Number": [],
        "Count": [],
        "NIF in Standard": [],
        "Standard Name": [],
        "Standard Short Name": []
    }

    for name, count in sorted_wrongNamesCount.items():
        name_split = name.split(" | ")
        name = name_split[0]
        identification_number = name_split[1]
        standard_name = name_split[2]
        standard_short_name = name_split[3]
        notCorrected["Name"].append(name)
        notCorrected["Identification Number"].append(identification_number)
        notCorrected["Count"].append(count)
        notCorrected["NIF in Standard"].append(identification_number in identificationNumber_name)
        notCorrected["Standard Name"].append(standard_name)
        notCorrected["Standard Short Name"].append(standard_short_name)

    print(f"\nSaving data about not corrected names in the Database analysis.db...")
    notCorrected_df = pd.DataFrame(notCorrected)
    table_notCorrected = f"{table}-notCorrected"
    # Eliminar a tabela se já existir (para trocar pela mais recente)
    cursor.execute(f"DROP TABLE IF EXISTS `{table_notCorrected}`")

    # Salvar o dataframe em formato sql table
    notCorrected_df.to_sql(table_notCorrected, conn, index=False)
    print("Done!")

    print(f"\nSaving corrections done to file {table}-corrections.csv and to the Database analysis.db...")
    corrections_df = pd.DataFrame(corrections)
    
    # Salvar o dataframe em formato csv
    corrections_df.to_csv(f"{table}-corrections.csv", sep=';', index=False)

    # Eliminar a tabela se já existir (para trocar pela mais recente)
    cursor.execute(f"DROP TABLE IF EXISTS `{table}`")

    # Salvar o dataframe em formato sql table
    corrections_df.to_sql(table, conn, index=False)
    print("Done!")

    conn.commit()
    conn.close()

    print(f"""\nEstatisticas:
        Já Corrigido = {already_corrected_count}
        Nomes Corrigidos = {name_corrected_count}
        Nomes e Identification Number Corrigido = {name_and_identificationNumber_corrected_count}
        Corrigidos com auxilio do mapa de sinonimos = {corrected_by_synonym_count}
        Não Corrigido = {not_corrected_count}
        Sem Identification_Number (not counting yet) = {no_identification_number_count} 
        Identification_Number Repetido --> Skipped = {repeated_identificationNumber_skipped_count}
        Percentagem de nomes corrigidos = {((already_corrected_count + name_and_identificationNumber_corrected_count + name_corrected_count + corrected_by_synonym_count) / len(df))*100:.3f}%
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


end_time = time.time()
elapsed_time = end_time - start_time
print(f"\nExecution time: {elapsed_time:.2f} seconds <=> {(elapsed_time/60.0):.2f} minutes <=> {(int(elapsed_time/3600) + ((elapsed_time/3600 - int(elapsed_time/3600))*60)/100):.2f} hours")
