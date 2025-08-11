import pandas as pd
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
standard_unique_names_file_path = os.path.join(BASE_DIR, "Standard-unique_names_count.json")
departure_unique_names_file_path = os.path.join(BASE_DIR, "Departure-unique_names_count.json")
transport_unique_names_file_path = os.path.join(BASE_DIR, "Transport-unique_names_count.json")

def create_dict_standard_unique_names_count(standard_data_frame):
    # Use value_counts() for efficient counting
    name_counts = standard_data_frame["name"].astype(str).value_counts()

    # Convert to native Python dict with int values to ensure JSON compatibility
    sorted_unique_names = {str(k): int(v) for k, v in name_counts.items()}

    # Write to file
    with open(standard_unique_names_file_path, "w", encoding="utf-8") as f:
        json.dump(sorted_unique_names, f, ensure_ascii=False, indent=4)


def create_dict_departure_unique_names_count(departure_data_frame):
    # Use value_counts() for efficient counting
    name_counts = departure_data_frame["name"].astype(str).value_counts()

    # Convert to native Python dict with int values to ensure JSON compatibility
    sorted_unique_names = {str(k): int(v) for k, v in name_counts.items()}

    # Write to file
    with open(departure_unique_names_file_path, "w", encoding="utf-8") as f:
        json.dump(sorted_unique_names, f, ensure_ascii=False, indent=4)


def create_dict_transport_unique_names_count(transport_data_frame):
    # Use value_counts() for efficient counting
    name_counts = transport_data_frame["name"].astype(str).value_counts()

    # Convert to native Python dict with int values to ensure JSON compatibility
    sorted_unique_names = {str(k): int(v) for k, v in name_counts.items()}

    # Write to file
    with open(transport_unique_names_file_path, "w", encoding="utf-8") as f:
        json.dump(sorted_unique_names, f, ensure_ascii=False, indent=4)
