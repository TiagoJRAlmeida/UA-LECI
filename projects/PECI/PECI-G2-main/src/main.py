import os
import json 
import Levenshtein
import time
from table_functions import *
from unique_names import create_dict_departure_unique_names,\
                        create_dict_transport_unique_names, \
                        create_dict_standard_unique_names
from Clustering.clustering import create_clusters, create_ground_truth_synonym_clusters, postprocess_by_region
from Clustering.accuracy_test import clustering_accuracy, average_inter_cluster_similarity, average_intra_cluster_similarity
from string_cleaning import clean_name, light_clean_name
from tqdm import tqdm
import random

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Update file paths to use BASE_DIR
id_to_name_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/Standard-id_to_name_map.json")
synonym_map_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/synonym_map.json")
final_synonym_map_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/final_synonym_map.json")
clusters_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/clusters.json")
postprocess_clusters_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/postprocess_clusters.json")
synonym_clusters_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/synonym_clusters.json")
predicted_clusters_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/predicted_clusters.json")
predicted_clusters_with_base_clusters_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/predicted_clusters_with_base_clusters.json")
standard_unique_names_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/Standard-unique_names.json")
departure_unique_names_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/Departure-unique_names.json")
transport_unique_names_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/Transport-unique_names.json")
cluster_index_standard_name_map_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/cluster_index_standard_name_map.json")
departure_corrected_dataset_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/Departure-corrected_dataset.csv")
transport_corrected_dataset_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/Transport-corrected_dataset.csv")

def create_dict_id_to_count(standard_data_frame, departure_data_frame, transport_data_frame):
    standard_identification_numbers_count = standard_data_frame["identification_number"].value_counts()
    departure_identification_numbers_count = departure_data_frame["identification_number"].value_counts()
    transport_identification_numbers_count = transport_data_frame["identification_number"].value_counts()

    id_to_count_map = {}

    for index in range(len(standard_data_frame)):
        identification_number = str(standard_data_frame.at[index, "identification_number"])
        if identification_number in id_to_count_map:
            continue
        else:
            identification_number_count = int(standard_identification_numbers_count.get(identification_number, 0) +\
                                        departure_identification_numbers_count.get(identification_number, 0) +\
                                        transport_identification_numbers_count.get(identification_number, 0))
            id_to_count_map[identification_number] = identification_number_count
    
    return id_to_count_map
        

def create_dict_id_to_name(standard_data_frame):
    id_to_name_map = {"Repetidos": {}}
    
    for index in range(len(standard_data_frame)):
        standard_name = str(standard_data_frame.at[index, "name"])
        light_cleaned_standard_name = light_clean_name(standard_name)
        identification_number = str(standard_data_frame.at[index, "identification_number"])

        if identification_number not in id_to_name_map:
            id_to_name_map[identification_number] = light_cleaned_standard_name
        elif id_to_name_map[identification_number] == light_cleaned_standard_name:
            continue
        else:
            id_to_name_map["Repetidos"][identification_number] = {
                "Standard Name": standard_name,
                "Light Cleaned Standard Name": light_cleaned_standard_name,
                "Original Standard Name": id_to_name_map[identification_number]
            }
        
    return id_to_name_map


def complete_ground_truth_synonym_map(synonym_map, data_frame, id_to_name_map, id_to_count_map):
    corrected_count = 0
    repetidos = id_to_name_map.get("Repetidos", set())

    for row in tqdm(data_frame.itertuples(index=False), desc="Processing Rows", unit="row"):
        row_name = str(row.name)
        identification_number = str(row.identification_number)

        if identification_number in repetidos:
            continue

        if row_name in synonym_map:
            corrected_count += 1
            continue

        if identification_number in id_to_name_map:
            standard_name = id_to_name_map[identification_number]
            light_cleaned_standard_name = light_clean_name(standard_name)
            cleaned_row_name = clean_name(row_name)
            identification_number = str(identification_number)
            identification_number_count = int(id_to_count_map[identification_number])

            if is_standard_variant(row_name, standard_name):
                entry = synonym_map.setdefault(cleaned_row_name, {})
                ids = entry.setdefault(light_cleaned_standard_name, [])
                if (identification_number, identification_number_count) not in ids:
                    ids.append((identification_number, identification_number_count))
                corrected_count += 1
            else:
                continue
        else:
            continue


    multiple_in_count = 0
    for variant_name in synonym_map:
        for standard_name in synonym_map[variant_name]:
            if len(synonym_map[variant_name][standard_name]) != 1:
                multiple_in_count += 1
                print(variant_name)

    print(f"\n{'-'*60}")
    print(f"Summary of Synonym Map Correspondence:")
    print(f"  - Total Rows Processed: {len(data_frame)}")
    print(f"  - Multiple Identification Number Count: {multiple_in_count}")
    print(f"  - Rows with Synonym Map Correspondence: {corrected_count}")
    print(f"  - Percentage: {(corrected_count / len(data_frame)) * 100:.2f}%")
    print(f"{'-'*60}")


    return synonym_map


def is_standard_variant(row_name, standard_name):
    cleaned_row_name = clean_name(row_name)
    cleaned_standard_name = clean_name(standard_name)

    # Check if row name matches the standard name
    if row_name == standard_name or cleaned_row_name in cleaned_standard_name:
        return True
    
    # Check if row name is similar to the standard name
    distance_threshold = len(cleaned_row_name) * 0.3
    distance_to_standard_name = Levenshtein.distance(cleaned_row_name, cleaned_standard_name) 
    if distance_to_standard_name <= distance_threshold:
        return True
    else:
        return False
    

def main():
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
    # if not os.path.exists(id_to_name_file_path):
    #     print("\n--- Creating Standard Name to ID Map ---")
    #     id_to_name_map = create_dict_id_to_name(standard_data_frame)
    #     with open(id_to_name_file_path, "w", encoding="utf-8") as f:
    #         json.dump(id_to_name_map, f, ensure_ascii=False, indent=4)
    #     print(f"--- Standard Name to ID Map Created and Saved to {id_to_name_file_path}! ---")
    # else:
    #     with open(id_to_name_file_path, "r", encoding="utf-8") as file:
    #         id_to_name_map = json.load(file)

    if not os.path.exists(standard_unique_names_file_path):
        print("\n--- Creating Standard Unique Names ---")
        cleaned_name_to_light_cleaned_name_map = create_dict_standard_unique_names(standard_data_frame)
        print(f"--- Standard Unique Names Created and Saved to {standard_unique_names_file_path}! ---")
    else:
        with open(standard_unique_names_file_path, "r", encoding="utf-8") as file:
            cleaned_name_to_light_cleaned_name_map = json.load(file)

    if not os.path.exists(departure_unique_names_file_path):
        print("\n--- Creating Departure Unique Names ---")
        departure_unique_names_set = set(create_dict_departure_unique_names(departure_data_frame))
        print(f"--- Departure Unique Names Created and Saved to {departure_unique_names_file_path}! ---")
    else:
        with open(departure_unique_names_file_path, "r", encoding="utf-8") as file:
            departure_unique_names_set = set(json.load(file))

    if not os.path.exists(transport_unique_names_file_path):
        print("\n--- Creating Transport Unique Names ---")
        transport_unique_names_set = set(create_dict_transport_unique_names(transport_data_frame))
        print(f"--- Transport Unique Names Created and Saved to {transport_unique_names_file_path}! ---")
    else:   
        with open(transport_unique_names_file_path, "r", encoding="utf-8") as file:
            transport_unique_names_set = set(json.load(file))


    id_to_count_map = create_dict_id_to_count(standard_data_frame, departure_data_frame, transport_data_frame)
    id_to_name_map = create_dict_id_to_name(standard_data_frame)
    with open(id_to_name_file_path, "w", encoding="utf-8") as f:
        json.dump(id_to_name_map, f, ensure_ascii=False, indent=4)

    ground_truth_synonym_map = {}    
    for index in range(len(standard_data_frame)):
        standard_name = str(standard_data_frame.at[index, "name"])
        cleaned_standard_name = clean_name(standard_name)
        identification_number = str(standard_data_frame.at[index, "identification_number"])
        identification_number_count = id_to_count_map[identification_number]

        if identification_number_count == 1:
            continue

        # Prepare the entry
        entry = ground_truth_synonym_map.setdefault(cleaned_standard_name, {})
        ids = entry.setdefault(cleaned_standard_name, [])

        # Only append if the full tuple is not already there
        id_tuple = (identification_number, identification_number_count)
        if id_tuple not in ids:
            ids.append(id_tuple)

    # Sort synonym_map by the number of entries in the inner dictionary (number of standard names)
    sorted_synonym_map = dict(sorted(ground_truth_synonym_map.items(), key=lambda item: -len(item[1])))

    with open(synonym_map_file_path, "w", encoding="utf-8") as f:
        json.dump(sorted_synonym_map, f, ensure_ascii=False, indent=4)

    print("\nDone!")

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


    print("\n--> Departure Table")
    ground_truth_synonym_map = complete_ground_truth_synonym_map(ground_truth_synonym_map, departure_data_frame, id_to_name_map, id_to_count_map)
    print("\n--> Transport Table")
    ground_truth_synonym_map = complete_ground_truth_synonym_map(ground_truth_synonym_map, transport_data_frame, id_to_name_map, id_to_count_map)
 
    # Sort synonym_map by the number of entries in the inner dictionary (number of standard names)
    sorted_synonym_map = dict(sorted(ground_truth_synonym_map.items(), key=lambda item: -len(item[1])))

    with open(synonym_map_file_path, "w", encoding="utf-8") as f:
        json.dump(sorted_synonym_map, f, ensure_ascii=False, indent=4)

    end_time = time.time()
    elapsed_time = end_time - start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    print(f"\nStep 1 Execution time: {elapsed_time:.2f} seconds --> {hours}h {minutes}m {seconds}s")
    #######################################################################################################


    # print("\nTransforming Synonym Map into clusters...")
    # NOTE: The synonym map is used as ground truth.
    synonym_cluster, synonym_cluster_names, cluster_index_standard_name_map = create_ground_truth_synonym_clusters(ground_truth_synonym_map) 
    with open(cluster_index_standard_name_map_file_path, "w", encoding="utf-8") as f:
        json.dump(cluster_index_standard_name_map, f, ensure_ascii=False, indent=4)
    sorted_synonym_cluster = sorted(synonym_cluster, key=lambda x: len(x), reverse=True)
    with open(synonym_clusters_file_path, "w", encoding="utf-8") as f:
        json.dump(sorted_synonym_cluster, f, ensure_ascii=False, indent=4)


    #######################################################################################################
    print("\n" + "#"*60)
    print("\nStep 2: Creating clusters")
    start_time = time.time()

    # print("\nCreating predicted clusters, with synonym clusters as base...")
    # with open(clusters_file_path, "r") as f:
    #     clusters = json.loads(f.read())
    clusters = create_clusters(names=(departure_unique_names_set | transport_unique_names_set), similarity_threshold=0.76, base_clusters=synonym_cluster)
    sorted_clusters = sorted(clusters, key=lambda x: len(x), reverse=True)
    with open(clusters_file_path, "w", encoding="utf-8") as f:
        json.dump(sorted_clusters, f, ensure_ascii=False, indent=4)
    print(f"Clusters saved to {clusters_file_path}!")
    print(f"Number of clusters: {len(clusters)}")
    print(f"Number of unique names in clusters: {len(set([name for cluster in clusters for name in cluster]))}")

    print("Post processing clusters by region")
    postprocess_clusters = postprocess_by_region(clusters)
    sorted_postprocess_clusters = sorted(postprocess_clusters, key=lambda x: len(x), reverse=True)
    with open(postprocess_clusters_file_path, "w", encoding="utf-8") as f:
        json.dump(sorted_postprocess_clusters, f, ensure_ascii=False, indent=4)
    print(f"Clusters saved to {postprocess_clusters_file_path}!")
    print(f"Number of clusters: {len(postprocess_clusters)}")
    print(f"Number of unique names in clusters: {len(set([name for cluster in postprocess_clusters for name in cluster]))}")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    print(f"\nStep 2 Execution time: {elapsed_time:.2f} seconds --> {hours}h {minutes}m {seconds}s")
    #######################################################################################################


    #######################################################################################################
    print("\n" + "#"*60)
    print("\nStep 3: Calculating expected cluster accuracy")
    start_time = time.time()
    
    intra_sim = average_intra_cluster_similarity(clusters)
    inter_sim = average_inter_cluster_similarity(clusters)
    print(f"\nAverage intra-cluster similarity: {intra_sim:.2f}")
    print(f"Average inter-cluster similarity: {inter_sim:.2f}")
    
    postprocess_intra_sim = average_intra_cluster_similarity(postprocess_clusters)
    postprocess_inter_sim = average_inter_cluster_similarity(postprocess_clusters)
    print(f"Average postprocess intra-cluster similarity: {postprocess_intra_sim:.2f}")
    print(f"Average postprocess inter-cluster similarity: {postprocess_inter_sim:.2f}")

    print("\n" + "-"*60)
    print("\n--> Version 1 - Predicted Clusters with no base clusters") 
    print("Creating predicted clusters...")
    predicted_clusters = create_clusters(names=synonym_cluster_names, similarity_threshold=0.76)
    predicted_clusters = postprocess_by_region(predicted_clusters)
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
    predicted_clusters_with_base_clusters = create_clusters(names=synonym_cluster_names, similarity_threshold=0.76, base_clusters=synonym_base_clusters)
    predicted_clusters_with_base_clusters = postprocess_by_region(predicted_clusters_with_base_clusters)
    sorted_predicted_clusters_with_base_clusters = sorted(predicted_clusters_with_base_clusters, key=lambda x: len(x), reverse=True)
    with open(predicted_clusters_with_base_clusters_file_path, "w", encoding="utf-8") as f:
        json.dump(sorted_predicted_clusters_with_base_clusters, f, ensure_ascii=False, indent=4)
        
    print("Evaluating accuracy...")
    predicted_cluster_evaluation = clustering_accuracy(synonym_cluster, predicted_clusters_with_base_clusters)
    print("\nPredicted Clusters Evaluation:")
    print(f"  - Precision: {int(predicted_cluster_evaluation['precision']*100)}%")
    print(f"  - Recall: {int(predicted_cluster_evaluation['recall']*100)}%")
    print(f"  - F1_score: {int(predicted_cluster_evaluation['f1_score']*100)}%")
    
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
    start_time = time.time()

    # Create cluster index to standard name map
    print("\nCreating cluster index to standard name map...")
    cluster_id_standard_map = {}
    for idx, cluster in enumerate(clusters):
        is_standard = False
        for name in cluster:
            if name in cleaned_name_to_light_cleaned_name_map:
                cluster_id_standard_map[idx] = cleaned_name_to_light_cleaned_name_map[name]
                is_standard = True
        if not is_standard:
            cluster_id_standard_map[idx] = cluster[0]

    with open(cluster_index_standard_name_map_file_path, "w", encoding="utf-8") as f:
        json.dump(cluster_id_standard_map, f, ensure_ascii=False, indent=4)


    final_version_synonym_map = {}
    print("\n--> Departure Table")
    for departure_name in departure_unique_names_set:
        if departure_name in final_version_synonym_map:
            continue
        for idx, cluster in enumerate(clusters):
            if departure_name in cluster:
                final_version_synonym_map[departure_name] = cluster_id_standard_map[idx]
                break

    print("\n--> Transport Table")
    for transport_name in transport_unique_names_set:
        if transport_name in final_version_synonym_map:
            continue
        for idx, cluster in enumerate(clusters):
            if transport_name in cluster:
                final_version_synonym_map[transport_name] = cluster_id_standard_map[idx]
                break

    with open(final_synonym_map_file_path, "w", encoding="utf-8") as f:
        json.dump(final_version_synonym_map, f, ensure_ascii=False, indent=4)

    end_time = time.time()
    elapsed_time = end_time - start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    print(f"\nStep 4 Execution time: {elapsed_time:.2f} seconds --> {hours}h {minutes}m {seconds}s")
    #######################################################################################################


    #######################################################################################################
    print("\n" + "#"*60)
    print("\n" + "Step 5: Correcting dataset with synonym map")
    start_time = time.time()

    # Process Departure Table
    corrected_rows = []
    print("\nProcessing Departure Table...")
    for row in departure_data_frame.itertuples(index=False):
        original_name = str(row.name)
        identification_number = str(row.identification_number)
        standard_name = final_version_synonym_map.get(clean_name(original_name), "No Match")
        corrected_rows.append({
            "Original Name": original_name,
            "Standard Name": standard_name,
            "Identification Number": identification_number,
            "Original Standard Name": "None" if identification_number not in id_to_name_map else id_to_name_map[identification_number]
        })

    corrected_df = pd.DataFrame(corrected_rows)
    corrected_df.to_csv(departure_corrected_dataset_file_path, index=False, encoding="utf-8")
    print(f"\nCorrected dataset saved to {departure_corrected_dataset_file_path}!")
    
    # Show unique counts
    unique_ids = corrected_df["Identification Number"].nunique()
    unique_std_names = corrected_df["Standard Name"].nunique()
    no_match_count = (corrected_df["Standard Name"] == "No Match").sum()
    print(f"Departure Table: {unique_ids} unique identification numbers")
    print(f"Departure Table: {unique_std_names} unique standard names")
    print(f"Departure Table: {no_match_count} standard names with 'No Match'")

    # Process Transport Table
    corrected_rows = []
    print("\nProcessing Transport Table...")
    for row in transport_data_frame.itertuples(index=False):
        original_name = str(row.name)
        identification_number = str(row.identification_number)
        standard_name = final_version_synonym_map.get(clean_name(original_name), "No Match")
        corrected_rows.append({
            "Original Name": original_name,
            "Standard Name": standard_name,
            "Identification Number": identification_number,
            "Original Standard Name": "None" if identification_number not in id_to_name_map else id_to_name_map[identification_number]
        })
        
    corrected_df = pd.DataFrame(corrected_rows)
    corrected_df.to_csv(transport_corrected_dataset_file_path, index=False, encoding="utf-8")
    print(f"\nCorrected dataset saved to {transport_corrected_dataset_file_path}!")

    # Show unique counts
    unique_ids = corrected_df["Identification Number"].nunique()
    unique_std_names = corrected_df["Standard Name"].nunique()
    no_match_count = (corrected_df["Standard Name"] == "No Match").sum()
    print(f"Transport Table: {unique_ids} unique identification numbers")
    print(f"Transport Table: {unique_std_names} unique standard names")
    print(f"Transport Table: {no_match_count} standard names with 'No Match'")

    end_time = time.time()
    elapsed_time = end_time - start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    print(f"\nStep 5 Execution time: {elapsed_time:.2f} seconds --> {hours}h {minutes}m {seconds}s")
    #######################################################################################################


    print("\n" + "#"*60)
    print("\n" + "End of the script")

if __name__ == '__main__':
    main()