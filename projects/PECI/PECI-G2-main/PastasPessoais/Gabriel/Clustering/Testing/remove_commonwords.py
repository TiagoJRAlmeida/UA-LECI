import json
from strings_manipulation import clean_name
import pycountry
import re

def remove_common(word):
    with open("manual_part_count.json","r") as file:
        word_count = json.loads(file.read())
    
    with open("abreviation.json","r") as file:
        abreviation = json.loads(file.read())

    common_words = [i for i in word_count.keys()]

    bad_words = {"rua","street","estrada","avenida","edif","largo","lda","av"}
    
    word = clean_name(word)

    for i in bad_words:
        if i in word:
            word = word[:word.find(i)] 

    word_split = word.split(" ")

    countries = {i.name.lower() for i in pycountry.countries}

    for i in range(len(word_split)):
        for j in countries:
                word_split[i] = re.sub(j,'',word_split[i])

    for i in range(len(word_split)):
        for j in abreviation.keys():
            word_split[i] = re.sub(j,abreviation[j] + " ",word_split[i])

    return "".join(i + " " for i in word_split)
