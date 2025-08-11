REGION_KEYWORDS = {
    # Full names
    'usa', 'uk', 'germany', 'greece', 'china', 'india', 'israel', 'egypt', 'uae',
    'turkey', 'saudi', 'france', 'spain', 'italy', 'canada', 'brazil', 'mexico', 'australia',
    'panama', 'japan', 'senegal', 'colombia', 'vietnam', 'indonesia', 'netherlands',
    'south africa', 'portugal', 'argentina', 'singapore', 'russia', 'poland', 'peru', 'chile',
    'morocco', 'algeria', 'kenya', 'tanzania', 'ghana', 'nigeria', 'costa rica', 'ecuador',
    'bolivia', 'uruguay', 'venezuela', 'honduras', 'guatemala', 'nicaragua', 'paraguay',
    'dominican', 'el salvador', 'lebanon', 'sri lanka', 'bangladesh', 'nepal', 'pakistan',
    'thailand', 'malaysia', 'myanmar', 'taiwan', 'hong kong', 'south korea', 'korea', 'mozambique',
    'angola', 'tunisia', 'libya', 'zambia', 'zimbabwe', 'cameroon', 'ethiopia', 'botswana', 'grecia', 
    'belgica', 'noruega', 'suecia', 'alemanha', 'irlanda', 'dinamarca', 'norway', 'denmark', 'franca',
    'espanha', 'marrocos', 'irlanda', 'bulgaria', 'estonia', 'paises baixos', 'britanica', 'coreia do sul',
    'italia', 'brasil', 

    # Cities or custom regions
    'dubai', 'riyadh', 'jeddah', 'cairo', 'doha', 'abu dhabi', 'amman', 'santiago',
    'barcelona', 'madrid', 'guadalajara', 'monterrey', 'puebla', 'lyon', 'porto', 'lisbon',
    'paris', 'milan', 'milano', 'napoli', 'rome', 'athens', 'sofia', 'bucharest', 'vienna',
    'warsaw', 'zagreb', 'brussels', 'oslo', 'stockholm', 'copenhagen', 'geneva', 'lausanne',
    'luxembourg', 'shanghai', 'beijing', 'shenzhen', 'qingdao', 'xiamen', 'tianjin', 'ilha do faial',
    'ilha do corvo', 'ilha terceira', 'ilha sao miguel', 'texas', 'hong kong', 'matosinhos', 'leixoes',
    'setubal', 'sesimbra', 'ponta delgada', 'setubalense', 'portimao', 'roque do pico', 'madalena do pico'

    # ISO Alpha-2 country codes
    'us', 'fr', 'de', 'pt', 'es', 'it', 'nl', 'be', 'se', 'no', 'fi', 'dk', 'pl', 'gr',
    'ro', 'bg', 'cz', 'hu', 'sk', 'si', 'at', 'ch', 'ie', 'ru', 'tr', 'cn', 'jp', 'kr', 'in',
    'id', 'th', 'my', 'vn', 'sg', 'ph', 'bd', 'pk', 'il', 'eg', 'sa', 'ae', 'qa', 'kw', 'dz',
    'ma', 'tn', 'ng', 'gh', 'za', 'zm', 'zw', 'cm', 'ke', 'tz',

    # ISO Alpha-3 codes (and common short customs abbreviations)
    'usa', 'mex', 'can', 'esp', 'bra', 'deu', 'fra', 'ita', 'prt', 'nld', 'bel', 'che', 'swe',
    'nor', 'fin', 'dnk', 'pol', 'grc', 'rou', 'bgr', 'cze', 'hun', 'svk', 'svn', 'aut', 'irl',
    'gbr', 'rus', 'tur', 'chn', 'jpn', 'kor', 'ind', 'idn', 'tha', 'mys', 'vnm', 'sgp', 'phl',
    'pak', 'bgd', 'isr', 'egy', 'sau', 'are', 'qat', 'kwt', 'dza', 'mar', 'tun', 'nga', 'gha',
    'zaf', 'zmb', 'zwe', 'cmr', 'ken', 'tza',

    # Seen in the clusters
    'esp', 'pt', 'po', 'sh', 'sur', 'sor', 'ne', 'lim', 'sen', 'del', 'mex', "spa", "viet", "chin"
}


import re

def extract_regions(name):
    name_lower = name.lower()
    
    # Garante que só vai buscar frases ou palavras inteiras (ex: 'ilha terceira', não 'sa' dentro de 'saude')
    regions = {
        region for region in REGION_KEYWORDS
        if re.search(rf'\b{re.escape(region)}\b', name_lower)
    }
    
    return regions if regions else {"default"}


UNIQUE_PEOPLE_NAMES = {
    'julio', 'miguel', 'manuel', 'domingos', 'joao', 'ricardo', 'silva', 'paulo', 'alverca', 'matos', 'carlos', 'dias', 
    'carvalho', 'de', 'monteiro', 'joel', 'maria', 'marques', 'joaquim', 'santos', 'torres', 'jorge', 'roberto', 'fernando',
    'machado', 'oliveira', 'pereira', 'martins', 'reis', 'rafael', 'dos', 'lima', 'rodrigues', 'teixeira', 'angeja', 'antonio', 
    'francisco', 'rouxinol', 'barbosa', 'ramos', 'ferreira', 'costa', 'luis', 'viegas', 'alberto', 'silveira', 'gomes', 'soares', 
    'ribeiro', 'lda', 'rilho', 'rodrigo', 'melo', 'ernesto', 'madeira', 'nascimento', 'moutela', 'rocha', 'alves', 'simoes', 
    'jose', 'pinto', 'almeida', 'filipe', 'mfigueiredo', 'figueiredo', 'engenheiro', 'fernandes', 'brito', 'pedro', 'mota', 'domingues',
    'mendes', 'conceicao', 'esteves', 'carmo', 'severo', 'lanca', 'jesus', 'trindade', 'casqueiro', 'coelho', 'carreira', 'guilherme',
    'vitor', 'mesquita', 'regateiro', 'batista', 'santana', 'cruz', 'vieira', 'patricio', 'raimundo', 'novais', 'do', 'o', 
    'assis', 'fmartins', 'valente', 'guimaraes', 'costa', 'medeiros', 'guerreiro', 'farinha', 'leandro', 'goncalves', 'abel', 'faria',
    'mena', 'antunes', 'sovelas', 'alfaiate', 'cunha', 'da', 'forreta', 'mourao', 'pinho', 'e', 'semiao', 'barreiros', 'azevedo',
    'paixao', 'galhardo', 'antero', 'amandio', 'smelro', 'biscaia', 'marrafa', 'correia', 'maia', 'campos', 'monte', 'barreira', 'pguedes',
    'branco', 'artur', 'paiva', 'ana', 'ines', 'catarina', 'david', 'beatriz', 'helena', 'andre', 'daniel',
    'tiago', 'claudia', 'lara', 'sara', 'nuno', 'sofia', 'marco', 'carla', 'albino',
    'patricia', 'bruno', 'tania', 'alexandre', 'rute', 'rita', 'isabel',
    'filipa', 'sandra', 'marta', 'susana', 'edgar', 'mariana', 'diogo',
    'nuno', 'eva', 'renato', 'raul', 'celia', 'victor', 'aline', 'simao',
    'ricardina', 'elisa', 'alina', 'lucas', 'moises', 'joana', 'leonor',
    'sergio', 'milene', 'carminho', 'telma', 'edna', 'rui', 'chagas', 'horta'
}

names = ["antonio oliveira despachante aduaneiro",
        "antonio oliveira dos santos catalao",
"joaquim jose felisbelo silva",
        "joaquim jose silva canas",
"jose eduardo rodrigues abreu",
        "jose eduardo costa abreu aguiar",
"joao jose baleizao barracha",
        "joao jose silva barros",
"rui manuel dos santos bacalhau",
        "rui manuel santos gaspar",
"rui miguel nunes silva",
        "rui miguel martins sousa e silva",
"olga maria simoes francisco",
        "olga maria costa carvalho",
"jose augusto lopes",
        "jose augusto barreiras",
"fernando manuel silva ttrovao",
        "fernando manuel santos angelo",
"jorge moreira raposo",
"antonio manuel cascais gomes",
        "antonio manuel gomes pila",
"pedro miguel vieira sousa ferreira catarino",
        "pedro miguel pereira brandao sousa matos",
"joao carlos pessoa alves garcia",
        "joao carlos peca nunes fonseca",
"manuel sebastiao cpeixoto e outro",
        "manuel sebastiao martins simoes",
"jose silva bandeira lda",
        "jose silva repolholda",
"joao miguel crujo lince uva",
        "joao miguel freitas monteiro",
"antonio da luz alves",
        "antonio da luz alves filhos lda",
"jose paulo silva jacome sousa",
        "jose paulo pereira sousa",
"joao agostinho silva oliveira",
        "joao agostinho cascais silva",
"carlos manuel fferreira",
        "carlos manuel luis flecha rodrigues",
"vitor manuel jacinto lopes",
        "vitor manuel lopes gramatinha",
"jose maria santos cabral",
        "jose maria cabral vozone",
"joaquim manuel conde marques silva",
        "joaquim manuel silva pita",
"jose carlos silva unipessoal lda",
        "jose carlos mateus lda",
"joao paulo caldeira tavira",
        "joao paulo freire portela",
"miguel nuno gourgel fonseca santos",
        "miguel nuno abastos santos",
"maria joao botelho martins alverca",
        "maria joao ferreira lrcorreia",
"joaquim antonio cavaco",
        "joaquim antonio urbano vaz",
"jose manuel pinto carapinha",
        "jose manuel elisbao pinto",
"mario miguel rocha santos",
        "mario miguel bandarra santos",
"manuel jose baeta da cruz",
        "manuel jose baeta purificano",
"joaquim duarte urmal filhos lda",
        "joaquim duarte urmal e filhos lda",
"pedro nuno rasteiro santos",
        "pedro nuno melo pessoa",
"joao henrique fernandes goncalves",
        "joao henrique militao fernandes",
"joaquim manuel borrego",
        "joaquim manuel vinagre boavida",
"joao pedro da silva pimenta vasconcelos",
        "joao pedro correia simoes travassos",
"jose manuel fortunato lda",
        "jose manuel msantos lda",
"jose francisco cruz catarino",
        "jose francisco sousa cruz",
"ana maria sotero sobatista",
        "ana maria jesus faria soares lopes",
"jose carlos santos lopes",
        "jose carlos lopes beirao",
"jose pedro peralta madeira",
        "jose pedro mendonca pereira",
"fernando manuel flsmbarbosa",
        "fernando manuel fpinto",
"acacio sousa",
"carlos jorge trincheiras delca",
"paulo alexandre ferreira gil pereira",
        "paulo alexandre pereira bento",
"joao antonio carvalho neto",
        "joao antonio mde melo bandeira",
"maria fatima josilva santos",
        "maria fatima costa guerreiro",
"joao paulo albino rafael",
        "joao paulo valerio melo",
"paulo jorge almeida teixeira lopes",
        "paulo jorge lobo pereira",
"sebastiao paulo e filhos lda",
        "sebastiao paulo e outros lda",
 "joao garcia despachante oficial",
        "joao garcia despachante oficial unipessoal lda",
"joao manuel amorim caxaria",
        "joao manuel duarte rodrigues",
"henrique joao cantoneiro",
        "henrique joao",
"armando jorge pereira lima",
        "armando jorge duarte silva santos",
"manuel augusto nsleal e outro",
        "manuel augusto domingos neto",
"pedro manuel santos forte faria",
        "pedro manuel sanches santos"
]


print(UNIQUE_PEOPLE_NAMES)
print(len(UNIQUE_PEOPLE_NAMES))
for name in names:
    unique_names = name.split()
    for un in unique_names:
        if un not in UNIQUE_PEOPLE_NAMES:
            UNIQUE_PEOPLE_NAMES.add(un)
    
print("\n" + "="*60 + "\n")
print(UNIQUE_PEOPLE_NAMES)
print(len(UNIQUE_PEOPLE_NAMES))


