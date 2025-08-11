import unicodedata
import unidecode
import re


UNIQUE_PEOPLE_NAMES = {'julio', 'miguel', 'manuel', 'domingos', 'joao', 'ricardo', 'silva', 'paulo', 'alverca', 'matos', 'carlos', 'dias', 
                       'carvalho', 'de', 'monteiro', 'joel', 'maria', 'marques', 'joaquim', 'santos', 'torres', 'jorge', 'roberto', 'fernando',
                         'machado', 'oliveira', 'pereira', 'martins', 'reis', 'rafael', 'dos', 'lima', 'rodrigues', 'teixeira', 'angeja', 'antonio', 
                         'francisco', 'rouxinol', 'barbosa', 'ramos', 'ferreira', 'costa', 'luis', 'viegas', 'alberto', 'silveira', 'gomes', 'soares', 
                         'ribeiro', 'lda', 'rilho', 'rodrigo', 'melo', 'ernesto', 'madeira', 'nascimento', 'moutela', 'rocha', 'alves', 'simoes', 
                         'jose', 'pinto', 'almeida'
}

STOP_WORDS = {"rua","street","estrada","avenida","edif","largo","lda","av"}

TRANSLATION_TABLE = {
    "ldarua": "lda rua",
    "to the order of": "",
    "the order of": "",
    "to te order": "",
    "to order": "",
    "to order of": "",
    "the order": "",   
}

def is_person_name(name):
    return all(n in UNIQUE_PEOPLE_NAMES for n in name.split())


def clean_name(name):
    name = unidecode.unidecode(name.lower())
    name = re.sub(r'-', ' - ', name)
    name = re.sub(r'\s+', ' ', name).strip()

    for k, v in TRANSLATION_TABLE.items():
        name = name.replace(k, v)
    
    words = name.split()
    for index, word in enumerate(words):
        if (word == "-" or word in STOP_WORDS) and index > 0:
            words = words[:index]  # remove everything before to and including the stopword
            break
    name = " ".join(words)

    # name = re.sub(r'\b(ltd|inc|llc|co|corp|company|sa|gmbh|plc)\b', '', name)
    name = re.sub(r'[^a-z0-9 ]+', '', name)
    return re.sub(r'\s+', ' ', name).strip()