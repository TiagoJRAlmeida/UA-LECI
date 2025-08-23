import json
import os
from string_cleaning import clean_name, light_clean_name

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
standard_unique_names_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/Standard-unique_names.json")
departure_unique_names_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/Departure-unique_names.json")
transport_unique_names_file_path = os.path.join(BASE_DIR, "AuxiliaryFiles/Transport-unique_names.json")


def create_dict_standard_unique_names(standard_data_frame):
    name_list = standard_data_frame["name"].astype(str).tolist()

    # Apply clean_name() and remove duplicates (unordered)
    unique_names = set(name_list)

    cleaned_name_to_light_cleaned_name_map = {}
    for name in unique_names:
        cleaned_name = clean_name(name)
        light_cleaned_name = light_clean_name(name)
        if cleaned_name not in cleaned_name_to_light_cleaned_name_map:
            cleaned_name_to_light_cleaned_name_map[cleaned_name] = light_cleaned_name

    # Write to file
    with open(standard_unique_names_file_path, "w", encoding="utf-8") as f:
        json.dump(cleaned_name_to_light_cleaned_name_map, f, ensure_ascii=False, indent=4)

    return cleaned_name_to_light_cleaned_name_map


def create_dict_departure_unique_names(departure_data_frame):
    name_list = departure_data_frame["name"].astype(str).tolist()

    # Apply clean_name() and remove duplicates (unordered)
    unique_cleaned_names = list(set(clean_name(name) for name in name_list))

    # Write to file
    with open(departure_unique_names_file_path, "w", encoding="utf-8") as f:
        json.dump(unique_cleaned_names, f, ensure_ascii=False, indent=4)

    return unique_cleaned_names


def create_dict_transport_unique_names(transport_data_frame):
    name_list = transport_data_frame["name"].astype(str).tolist()

    # Apply clean_name() and remove duplicates (unordered)
    unique_cleaned_names = list(set(clean_name(name) for name in name_list))

    # Write to file
    with open(transport_unique_names_file_path, "w", encoding="utf-8") as f:
        json.dump(unique_cleaned_names, f, ensure_ascii=False, indent=4)

    return unique_cleaned_names
