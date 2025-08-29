import unidecode
import re


LEGAL_PREFIX = {
    'plc', 'inc', 'company', 'tic', 'dis', 'sti', 'ltd', 'sirketi', 'ic', 'spa', 've', 'sa', 'ltdsti', 
    'san', 'as', 'pte', 'bv', 'ticaret', 'anonim', 'co', 'llc', 'gmbh', 'corp', 'ltda'
}

UNIQUE_PEOPLE_NAMES = {
    'julio', 'miguel', 'manuel', 'domingos', 'joao', 'ricardo', 'silva', 'paulo', 'alverca', 'matos', 'carlos', 'dias', 
    'carvalho', 'de', 'monteiro', 'joel', 'maria', 'marques', 'joaquim', 'santos', 'torres', 'jorge', 'roberto', 'fernando',
    'machado', 'oliveira', 'pereira', 'martins', 'reis', 'rafael', 'dos', 'lima', 'rodrigues', 'teixeira', 'angeja', 'antonio', 
    'francisco', 'rouxinol', 'barbosa', 'ramos', 'ferreira', 'costa', 'luis', 'viegas', 'alberto', 'silveira', 'gomes', 'soares', 
    'ribeiro', 'lda', 'rilho', 'rodrigo', 'melo', 'ernesto', 'madeira', 'nascimento', 'moutela', 'rocha', 'alves', 'simoes', 
    'jose', 'pinto', 'almeida'
}

STOP_WORDS = {
    "rua","street","estrada","avenida","edif","largo","av"
}

TRANSLATION_TABLE = {
    r"\bldaav\b": "lda av",
    r"\bldarua\b": "lda rua",
    r"\bldaas\b": "lda as",
    r"\bto the order of\b": "",
    r"\bthe order of\b": "",
    r"\bto te order\b": "",
    r"\bto order\b": "",
    r"\bto order of\b": "",
    r"\bthe order\b": "",
    r"\bindustria e comercio\b": "",
    r"\bcomercio e industria\b": "",
    r"\bindustria\b": "",
    r"\bimportacao e exportacao\b": "",
    r"\bimportacao\b": "",
    r"\bexportacao\b": "",
    r"\bsa de cv\b": "",
    r"\brl de cv\b": "",
    r"\bas agents\b": "",
    r"\bsociedad anonima\b": "sa",
    r"\bltdsti\b": "ltd sti",
    r"\bspz oo\b": "sp z oo",
    r"\bc h\b": "ch",
    r"\bairsea\b": "air sea",
    r"\bltdaav\b": "ltda av",
    r"\btran\b": "transitarios",
    r"\btrans\b": "transitarios",
    r"\btransitariossociedade\b": "transitarios sociedade",
    r"\bj f\b": "jf"
}

TRANSLATION_REGEX = [
    (re.compile(pattern), replacement)
    for pattern, replacement in sorted(TRANSLATION_TABLE.items(), key=lambda x: -len(x[0]))
]


def clean_name(name):
    name = unidecode.unidecode(name.lower())
    name = re.sub(r'-', ' - ', name)
    name = re.sub(r'[.,]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()

    for pattern, repl in TRANSLATION_REGEX:
        name = pattern.sub(repl, name)

    words = name.split()
    for index, word in enumerate(words):
        if word in STOP_WORDS and index > 0:
            words = words[:index]
            break
    name = " ".join(words)

    name = re.sub(r'[^a-z0-9 ]+', '', name)
    return re.sub(r'\s+', ' ', name).strip()


def light_clean_name(name):
    name = unidecode.unidecode(name.lower())
    name = re.sub(r'-', ' - ', name)
    name = re.sub(r'[^a-z0-9 ]+', '', name)
    return re.sub(r'\s+', ' ', name).strip()


def is_person_name(name):
    return all(n in UNIQUE_PEOPLE_NAMES for n in name.split())