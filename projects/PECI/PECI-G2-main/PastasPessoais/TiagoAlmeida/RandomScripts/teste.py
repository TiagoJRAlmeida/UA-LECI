import re

# def intersect_name_lists(word_dict, name):
#     words = name.split()  # Split the name into words
#     result_sets = [set(word_dict[word]) for word in words if word in word_dict]  # Get sets for matching words
    
#     if not result_sets:
#         return None  # No words found in dictionary
    
#     final_set = set()
#     for sets in result_sets:
    
#     return set.intersection(*result_sets)  # Intersect all sets

# Example usage
# word_dict = {
#     "John": ["John Doe", "John Smith", "John Wick"],
#     "Doe": ["John Doe", "Jane Doe"],
#     "Jane": ["Jane Doe", "Jane Austen"],
#     "s.a": ["Portugal s.a", "Spain s.a", "USA s.a", "Canada s.a"]
# }

# name = "John Doe s.a"
# result = intersect_name_lists(word_dict, name)
# print(result)

import unicodedata

def remove_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def clean_string(s):
    s = remove_accents(s)  # Remove accents (ç -> c, ã -> a, etc.)
    return re.sub(r'[^a-zA-Z0-9 ]', '', s).lower()


test_name = "T1ag.o Alm*eida CONSTRUÇÃO"

print(clean_string(test_name))