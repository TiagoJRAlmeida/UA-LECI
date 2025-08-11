import pandas as pd
import os
import json 
import Levenshtein
import time
import pickle
from table_functions import *
from file_manipulation import *
# from strings_manipulation import *
from UniqueNamesScripts.unique_names import create_dict_standard_unique_names_count,\
                                            create_dict_departure_unique_names_count,\
                                            create_dict_transport_unique_names_count
from Clustering.clustering import create_clusters, create_synonym_clusters
from Clustering.accuracy_test import clustering_accuracy
from tqdm import tqdm
import random


# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Update file paths to use BASE_DIR
standard_minhash_lsh_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/Standard-minhashlsh.pkl")
standard_words_to_names_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/Standard-words_names.json")
standard_unique_words_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/Standard-unique_words.txt")
id_to_name_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/Standard-id_to_name_map.json")
name_to_id_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/Standard-name_to_id_map.json")
possible_standard_names_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/possible_standard_names.txt")
synonym_map_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/synonym_map.json")
clusters_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/clusters.json")
synonym_clusters_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/synonym_clusters.json")
predicted_clusters_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/predicted_clusters.json")
predicted_clusters_with_base_clusters_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/predicted_clusters_with_base_clusters.json")
standard_unique_names_file_path = os.path.join(BASE_DIR, "UniqueNamesScripts/Standard-unique_names_count.json")
departure_unique_names_file_path = os.path.join(BASE_DIR, "UniqueNamesScripts/Departure-unique_names_count.json")
transport_unique_names_file_path = os.path.join(BASE_DIR, "UniqueNamesScripts/Transport-unique_names_count.json")

# NOTE: This function is not used in the current version of the code.
# This function finds the best match between a list of candidate names 
# given by the minhash lsh. Since we are not using the minhash lsh in the current version of the code,
# we are not using this function either. For more information, check the NOTE above the function "correct_name_whithout_standard". 
def find_best_match(row_name, candidate_names):
    if len(candidate_names) == 0:
        return []
    
    cleaned_row_name = clean_name(row_name)
    if cleaned_row_name == "":
        return []
    
    best_candidate = candidate_names[0]
    max_distance_threshold = (len(cleaned_row_name) * 0.3)
    simplified_best_candidate = clean_name(row_name)
    best_distance = Levenshtein.distance(cleaned_row_name, simplified_best_candidate)

    if len(candidate_names) == 1:
        if best_distance >= max_distance_threshold:
            return []
        return best_candidate
    
    for candidate in candidate_names[1:]:
        simplified_candidate = clean_name(row_name)
        current_distance = Levenshtein.distance(cleaned_row_name, simplified_candidate)
        if current_distance < best_distance:
            best_distance = current_distance
            best_candidate = candidate
    
    if best_distance >= max_distance_threshold:
        return []
    return best_candidate


def process_table_rows(data_frame):
    global corrected_count, synonym_map, non_standard_name_set, id_to_name_map, name_to_id_map, minhash_lsh

    corrected_count = 0
    possible_standard_names = set()

    for index in tqdm(range(len(data_frame)), desc="Processing Rows", unit="row"):
        row_name = str(data_frame.at[index, "name"])
        identification_number = str(data_frame.at[index, "identification_number"])

        # Skip rows with duplicate identification numbers in the standard
        if identification_number in id_to_name_map["Repetidos"]:
            continue
        
        # Correct rows with names in the synonym map
        if row_name in synonym_map:
            corrected_count += 1
            continue

        # Skip rows with non-standard names
        if row_name in non_standard_name_set:
            continue

        # Correct rows with identification numbers in the standard
        if identification_number in id_to_name_map:
            if not correct_name_with_standard(row_name, identification_number):
                possible_standard_names.add(row_name)
            continue

        # Handle rows without identification numbers in the standard
        else:
            # Why we are not using this function? Check the NOTE above the function to understand.
            # correct_name_without_standard(row_name)
            non_standard_name_set.add(row_name)
            continue

    print(f"\n{'-'*60}")
    print(f"Summary of Synonym Map Correspondence:")
    print(f"  - Total Rows Processed: {len(data_frame)}")
    print(f"  - Rows with Synonym Map Correspondence: {corrected_count}")
    print(f"  - Percentage: {(corrected_count / len(data_frame)) * 100:.2f}%")
    print(f"{'-'*60}")

    return possible_standard_names


def correct_name_with_standard(row_name, identification_number):
    global corrected_count, synonym_map, non_standard_name_set, id_to_name_map, name_to_id_map, minhash_lsh

    standard_name = id_to_name_map[identification_number][0]
    standard_short_name = id_to_name_map[identification_number][1]
    cleaned_row_name = clean_name(row_name)
    cleaned_standard_name = clean_name(standard_name)
    cleaned_standard_short_name = clean_name(standard_short_name)

    # Check if row name matches the standard name
    if row_name == standard_name or cleaned_row_name in cleaned_standard_name or\
    row_name == standard_short_name or cleaned_row_name in cleaned_standard_short_name:
        synonym_map[row_name] = [standard_name, identification_number]
        corrected_count += 1
        return True
    
    max_distance_threshold = len(cleaned_row_name) * 0.3
    distance_to_standard_name = Levenshtein.distance(cleaned_row_name, cleaned_standard_name) 
    distance_to_standard_short_name = Levenshtein.distance(cleaned_row_name, cleaned_standard_short_name)

    # Check if row name is similar to the standard name
    if distance_to_standard_name <= max_distance_threshold or distance_to_standard_short_name <= max_distance_threshold:
        synonym_map[row_name] = [standard_name, identification_number]
        corrected_count += 1
        return True
    
    else:
        non_standard_name_set.add(row_name)
        return False
        # NOTE: Ideally we would use the minhash lsh for further search (commented out code).
        # However, the minhash lsh is not used in the current version of the code.
        # For more information, check the NOTE above the function "correct_name_whithout_standard".
        
        # possible_names = minhash_lsh.query(get_minhash(clean_name(row_name)))
        # best_match = find_best_match(row_name, possible_names, unique_words_set)
        
        # if not best_match:
        #     non_standard_name_set.add(row_name)
        #     return False
        # else: 
        #     if best_match == standard_name or best_match == standard_short_name:
        #         synonym_map[row_name] = [standard_name, identification_number]
        #         corrected_count += 1
        #         return True
        #     else:
        #         synonym_map[row_name] = [best_match, name_to_id_map[best_match][0]]
        #         corrected_count += 1
        #         return True


# NOTE: This function is not used in the current version of the code.
# This is due to the fact that the synonym map must be as correct as possible, (its used as ground truth)
# so we need to define a accuracy method before applying minhash. (as to not have errors) 
def correct_name_without_standard(row_name):
    global corrected_count, synonym_map, non_standard_name_set, name_to_id_map, minhash_lsh

    possible_names = minhash_lsh.query(get_minhash(clean_name(row_name)))
    best_match = find_best_match(row_name, possible_names, unique_words_set)

    if not best_match:
        non_standard_name_set.add(row_name)
        return False
    else:
        synonym_map[row_name] = [best_match, name_to_id_map[best_match][0]]
        corrected_count += 1
        return True


def setup_auxiliary_files(standard_data_frame, departure_data_frame, transport_data_frame):
    # Ensure all files are created in the same directory as the script
    if not os.path.exists(standard_unique_names_file_path):
        print("\n--- Creating Standard Unique Names Count ---")
        create_dict_standard_unique_names_count(standard_data_frame)
        print(f"--- Standard Unique Names Count Created and Saved to {standard_unique_names_file_path}! ---")

    if not os.path.exists(departure_unique_names_file_path):
        print("\n--- Creating Departure Unique Names Count ---")
        create_dict_departure_unique_names_count(departure_data_frame)
        print(f"--- Departure Unique Names Count Created and Saved to {departure_unique_names_file_path}! ---")

    if not os.path.exists(transport_unique_names_file_path):
        print("\n--- Creating Transport Unique Names Count ---")
        create_dict_transport_unique_names_count(transport_data_frame)
        print(f"--- Transport Unique Names Count Created and Saved to {transport_unique_names_file_path}! ---")

    if not os.path.exists(standard_minhash_lsh_file_path):
        print("\n--- Creating MinHashLSH ---")
        minhash_lsh = create_minHashLSH_table(standard_data_frame)
        with open(standard_minhash_lsh_file_path, "wb") as file:
            pickle.dump(minhash_lsh, file)
        print(f"--- MinHashLSH Created and Saved to {standard_minhash_lsh_file_path}! ---")


def main():
    global id_to_name_map, name_to_id_map, synonym_map, unique_words_set, minhash_lsh, non_standard_name_set

    #######################################################################################################
    print("\n" + "#"*60)
    print("\nStep 0: Setup Auxiliary Files")
    start_time = time.time()


    # Load tables
    print("\nLoading Standard Table...")    
    standard_data_frame = read_standard_table()
    print("Done!")

    print("\nLoading Departure Table...")
    departure_data_frame = read_departure_table()
    print("Done!")

    print("\nLoading Transport Table...")
    transport_data_frame = read_transport_table()
    print("Done!")
    
    print("\nSetting up auxiliary files and data structures...")
    setup_auxiliary_files(standard_data_frame, departure_data_frame, transport_data_frame)
    id_to_name_map = create_dict_id_to_name(standard_data_frame)
    name_to_id_map = create_dict_name_to_id(standard_data_frame)
    standard_words = create_dict_standard_words()
    unique_words_set = create_set_unique_words(standard_words)
    with open(standard_unique_names_file_path, "r", encoding="utf-8") as file:
        standard_unique_names_set = set(json.load(file).keys())
    with open(departure_unique_names_file_path, "r", encoding="utf-8") as file:
        departure_unique_names_set = set(json.load(file).keys())
    with open(transport_unique_names_file_path, "r", encoding="utf-8") as file:
        transport_unique_names_set = set(json.load(file).keys())

    with open(standard_minhash_lsh_file_path, "rb") as file:
        minhash_lsh = pickle.load(file)

    # Initialize synonym map
    synonym_map = {}
    for name in standard_unique_names_set:
        synonym_map[name] = [name, name_to_id_map[name][0]]
    non_standard_name_set = set()

    print("Done!")
    

    end_time = time.time()
    elapsed_time = end_time - start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    print(f"\nStep 0 Execution time: {elapsed_time:.2f} seconds --> {hours}h {minutes}m {seconds}s")
    #######################################################################################################


    #######################################################################################################
    print("\n" + "#"*60)
    print("\nStep 1: Creating First version of the Synonym Map")
    start_time = time.time()


    possible_standard_names = set()
    print("\n--> Departure Table")
    possible_standard_names.update(process_table_rows(departure_data_frame))
    print("\n--> Transport Table")
    possible_standard_names.update(process_table_rows(transport_data_frame))

    with open(synonym_map_file_path, "w", encoding="utf-8") as f:
        json.dump(synonym_map, f, ensure_ascii=False, indent=4)


    end_time = time.time()
    elapsed_time = end_time - start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    print(f"\nStep 1 Execution time: {elapsed_time:.2f} seconds --> {hours}h {minutes}m {seconds}s")
    #######################################################################################################


    #######################################################################################################
    print("\n" + "#"*60)
    print("\nStep 2: Calculating expected cluster accuracy")
    start_time = time.time()


    print("\nTransforming Synonym Map into clusters...")
    # NOTE: The synonym map is used as ground truth.
    # For more information about this function check the NOTE above the function "create_synonym_clusters()" 
    synonym_cluster, synonym_cluster_names, cluster_index_standard_name_map = create_synonym_clusters(synonym_map) 
    sorted_synonym_cluster = sorted(synonym_cluster, key=lambda x: len(x), reverse=True)
    with open(synonym_clusters_file_path, "w", encoding="utf-8") as f:
        json.dump(sorted_synonym_cluster, f, ensure_ascii=False, indent=4)

    
    print("\n" + "-"*60)


    print("\n--> Version 1 - Predicted Clusters with no base clusters") 
    
    print("Creating predicted clusters...")
    predicted_clusters = create_clusters(names=synonym_cluster_names)
    sorted_predicted_clusters = sorted(predicted_clusters, key=lambda x: len(x), reverse=True)
    with open(predicted_clusters_file_path, "w", encoding="utf-8") as f:
        json.dump(sorted_predicted_clusters, f, ensure_ascii=False, indent=4)
    
    print("Evaluating accuracy...")
    predicted_cluster_evaluation = clustering_accuracy(synonym_cluster, predicted_clusters)
    print("\nPredicted Clusters Evaluation:")
    print(f"  - Precision: {int(predicted_cluster_evaluation['precision']*100)}%")
    print(f"  - Recall: {int(predicted_cluster_evaluation['recall']*100)}%")
    print(f"  - F1_score: {int(predicted_cluster_evaluation['f1_score']*100)}%")


    print("\n" + "-"*60)


    print("\n--> Version 2 - Predicted Clusters with base clusters (50% of the synonym clusters)")
    print("Randomly selecting 50% of the synonym clusters...")
    base_percent = 0.5
    synonym_base_clusters = synonym_cluster.copy()
    names_to_add = set()
    for i in range(int(len(synonym_cluster) * base_percent)):
        random_index = random.randint(0, len(synonym_base_clusters)-1)
        removed_cluster = synonym_base_clusters.pop(random_index)
        names_to_add.update(set(removed_cluster))
    
    print("Creating predicted clusters...")
    predicted_clusters_with_base_clusters = create_clusters(names=synonym_cluster_names, base_clusters=synonym_base_clusters)
    sorted_predicted_clusters_with_base_clusters = sorted(predicted_clusters_with_base_clusters, key=lambda x: len(x), reverse=True)
    with open(predicted_clusters_with_base_clusters_file_path, "w", encoding="utf-8") as f:
        json.dump(sorted_predicted_clusters_with_base_clusters, f, ensure_ascii=False, indent=4)
        
    print("Evaluating accuracy...")
    predicted_cluster_evaluation = clustering_accuracy(synonym_cluster, predicted_clusters_with_base_clusters)
    print("\nPredicted Clusters Evaluation:")
    print(f"  - Precision: {int(predicted_cluster_evaluation['precision']*100)}%")
    print(f"  - Recall: {int(predicted_cluster_evaluation['recall']*100)}%")
    print(f"  - F1_score: {int(predicted_cluster_evaluation['f1_score']*100)}%")
    print("Creating predicted clusters...")
    
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    print(f"\nStep 2 Execution time: {elapsed_time:.2f} seconds --> {hours}h {minutes}m {seconds}s")
    #######################################################################################################


    #######################################################################################################
    print("\n" + "#"*60)
    print("\nStep 3: Creating actual clusters")
    start_time = time.time()


    print("\nCreating predicted clusters, with synonym clusters as base...")
    clusters = create_clusters(names=(departure_unique_names_set | transport_unique_names_set), base_clusters=synonym_cluster)
    sorted_clusters = sorted(clusters, key=lambda x: len(x), reverse=True)
    with open(clusters_file_path, "w", encoding="utf-8") as f:
        json.dump(sorted_clusters, f, ensure_ascii=False, indent=4)
    print(f"Clusters saved to {clusters_file_path}!")
    print(f"Number of clusters: {len(clusters)}")
    print(f"Number of unique names in clusters: {len(set([name for cluster in clusters for name in cluster]))}")
    
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    print(f"\nStep 3 Execution time: {elapsed_time:.2f} seconds --> {hours}h {minutes}m {seconds}s")
    #######################################################################################################


    #######################################################################################################
    print("\n" + "#"*60)
    print("\n" + "Step 4: Creating final synonym map")
    print("\n" + "Not done yet...")
    #######################################################################################################


    #######################################################################################################
    print("\n" + "#"*60)
    print("\n" + "Step 5: Correcting dataset with synonym map")
    print("\n" + "Not done yet...")
    #######################################################################################################


    print("\n" + "#"*60)
    print("\n" + "End of the script")

if __name__ == '__main__':
    main()