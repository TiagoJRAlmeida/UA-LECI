import re
import unicodedata
from itertools import combinations
import json
import Levenshtein


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

    print(f"\nDinamic Limit for Distance for {row_name}: {(len(row_name) * 0.9):.2f}")
    if len(lists) == 1:
        print(f"""Best Distance for {row_name}: {current_best_distance}""")
        if current_best_distance >= limit_distance:
            return []
        return lists[0]
    
    for possible_best in lists[1:]:
        current_distance = Levenshtein.distance(row_name, possible_best)
        if current_distance < current_best_distance:
            current_best_distance = current_distance
            current_best = possible_best
    
    print(f"""Best Distance for {row_name}: {current_best_distance}""")
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
        print(f"Word <{word}> is unique: {word in unique_words}")
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


def main(name_test, unique_words, words_names):
    print("\n")
    print("-"*90)
    print(f"\nInitial Name: {name_test}")

    cleaned_name_test = clean_row_name(name_test)
    print(f"\nAfter Cleaning: {cleaned_name_test}")

    reformated_cleaned_name_test = reformat_row_name(unique_words, cleaned_name_test)
    print(f"\nAfter reformating: {reformated_cleaned_name_test}")

    unique_words_lists = get_unique_words_lists(words_names, reformated_cleaned_name_test)
    possible_result = find_possible_match(name_test, unique_words_lists)
    if possible_result != None:
        print(f"\nPossible results: {possible_result}")  
        return  
    possible_result = get_best_result(name_test, list(max_intersection(unique_words_lists)[1]))
    print(f"\nPossible results: {possible_result}")


filename = "new_protocol/Departure-unique_words.txt"
unique_words = read_unique_words_from_file(filename)

# Abrir o dicionário words_names.json
with open('new_protocol/Departure-words_names.json', 'r', encoding="utf-8") as file:
    words_names = json.load(file)


test_name1 = "IKEA PURCHASING SERVICES (US) INC"
test_name2 = "OREY COMERCIO E NAVEGACAO, S.A."

main(test_name1, unique_words, words_names)
main(test_name2, unique_words, words_names)
