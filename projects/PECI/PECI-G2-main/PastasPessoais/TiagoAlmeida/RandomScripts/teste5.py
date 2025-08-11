import unicodedata
import re


translation_table = str.maketrans({
    ".": "",   # Remove dots
    "_": "",   # Remove underscores
    "-": " ",  # Replace hyphens with space
    ",": " ",  # Replace commas with space
    "\"": "",  # Remove double quotes
    "(": "",   # Remove opening parenthesis
    ")": "",   # Remove closing parenthesis
    "/": " ",
})


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


def remove_non_unique_words(name, unique_words):
    unique_words = set(unique_words)  # Convert to set for faster lookup (if not already a set)
    return " ".join(word for word in name.split() if word in unique_words)

unique_words = {"apple", "banana", "grape"}  
name = "apple orange banana kiwi grape"  
print(remove_non_unique_words(name, unique_words))

name = "kiwi orange"
print(remove_non_unique_words(name, unique_words) == "")


name = "Orey Comércio e Navegação, S.A."
print(simplify_name(name).split())


name = "Hugo Maria Lupi D´Orey"
print(simplify_name(name))
print(simplify_name("Hugo Maria Lupi D´Orey"))


def normalize_name(name: str) -> str:
    # Convert to lowercase
    name = name.lower()
    # Remove diacritics
    name = ''.join(
        c for c in unicodedata.normalize('NFKD', name) if not unicodedata.combining(c)
    )
    # Replace special apostrophe with normal one and remove it
    name = name.replace("´", "")
    return name

# Example usage
name = "Hugo Maria Lupi D´Orey"
normalized_name = normalize_name(name)
print(normalized_name)

for char in "DOrey":
    print(f"Character {char} is equal to ´ : {char == "´"}")


def clean_name(name):
    # Remove acentos e caracteres especiais
    name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
    
    # Converte tudo para minúsculas
    name = name.lower()
    
    # Remove todos os espaços
    name = name.replace(" ", "")
    
    # Remove caracteres especiais como "-", ";", ".", "_", etc.
    name = re.sub(r'[^a-z0-9]', '', name)
    
    return name


print(clean_name("KUEHNE   NAGEL, INC."))