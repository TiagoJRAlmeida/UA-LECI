from string_cleaning import clean_name

def create_synonym_map(standard_data_frame, id_to_count_map):
    synonym_map = {}    
    for index in range(len(standard_data_frame)):
        standard_name = str(standard_data_frame.at[index, "name"])
        cleaned_standard_name = clean_name(standard_name)
        light_cleaned_standard_name = clean_name(standard_name)
        identification_number = str(standard_data_frame.at[index, "identification_number"])
        identification_number_count = id_to_count_map[identification_number]

        if identification_number_count == 1:
            continue

        # Prepare the entry
        entry = synonym_map.setdefault(cleaned_standard_name, {})
        ids = entry.setdefault(light_cleaned_standard_name, [])

        # Only append if the full tuple is not already there
        id_tuple = (identification_number, identification_number_count)
        if id_tuple not in ids:
            ids.append(id_tuple)

    # Sort synonym_map by the number of entries in the inner dictionary (number of standard names)
    sorted_synonym_map = dict(sorted(synonym_map.items(), key=lambda item: -len(item[1])))

    #with open(synonym_map_file_path, "w", encoding="utf-8") as f:
    #    json.dump(sorted_synonym_map, f, ensure_ascii=False, indent=4)