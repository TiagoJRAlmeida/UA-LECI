import json
from strings_manipulation import clean_name
#import pycountry

def remove_common(word):
    with open("manual_part_count.json","r") as file:
        word_count = json.loads(file.read())

    common_words = [i for i in word_count.keys()]
    
    word = clean_name(word)

    word_split = word.split(" ")

    return "".join(i + " " for i in word_split if i not in common_words)
