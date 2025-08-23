import unicodedata
import re


def simplify_name(name):
    simplified_name = ""
    for char in name:
        if char == "´" or char == "`" or char == "’":
            simplified_name += ""
        else:
            simplified_name += char

    # Remove acentos e caracteres especiais
    simplified_name = unicodedata.normalize('NFKD', simplified_name).encode('ASCII', 'ignore').decode('ASCII')

    # Converte tudo para minúsculas
    simplified_name = simplified_name.lower()

    return simplified_name.translate(translation_table)


translation_table = str.maketrans({
        ".": "",   # Remove dots
        "_": "",   # Remove underscores
        "-": " ",  # Replace hyphens with space
        ",": " ",   # Replace commas with space
        "\"": "",  # Remove double quotes
        "(": "",   # Remove opening parenthesis
        ")": "",    # Remove closing parenthesis
        "/": " "
    })


def clean_name(name):
    # Remove acentos e caracteres especiais
    name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
    
    # Converte tudo para minúsculas
    name = name.lower()
    
    # Transforma caracteres especiais
    name = name.translate(translation_table)
    
    # Remove numeros
    name = re.sub(r'\d', '', name)
    
    return ' '.join(name.split()) # Remove os espaços extra


def remove_non_unique_words(name, unique_words):
    return " ".join(word for word in name.split() if word in unique_words)