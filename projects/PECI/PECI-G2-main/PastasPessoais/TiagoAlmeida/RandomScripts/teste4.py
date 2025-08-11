from datasketch import MinHash, MinHashLSH

# Lista de nomes de empresas para padronizar
nomes_empresas = [
    "Microsoft Corporation",
    "MicroSoft Corp",
    "Apple Inc.",
    "Apple Incorporated",
    "Google LLC",
    "Alphabet Inc.",
    "Amazon.com, Inc.",
    "Amazon Inc"
]

# Criar um índice LSH para encontrar nomes similares rapidamente
lsh = MinHashLSH(threshold=0.7, num_perm=128)

# Dicionário para armazenar MinHashes
minhashes = {}

def get_shingles(text, n=2):
    """Gera shingles (n-grams) de tamanho n a partir do texto."""
    text = text.lower().replace(",", "").replace(".", "")  # Normaliza
    return [text[i:i+n] for i in range(len(text) - n + 1)]

# Criar MinHashes usando shingles de 3 caracteres
for nome in nomes_empresas:
    m = MinHash(num_perm=128)
    for shingle in get_shingles(nome, n=2):
        m.update(shingle.encode('utf8'))
    lsh.insert(nome, m)
    minhashes[nome] = m

# Verificar quais nomes são semelhantes
consulta = "Microsoft Corp"  # Nome a verificar
m_query = MinHash(num_perm=128)
for shingle in get_shingles(consulta, n=2):
    m_query.update(shingle.encode('utf8'))

# Procurar no LSH
resultados = lsh.query(m_query)


print(f"Nomes semelhantes a '{consulta}': {resultados}")
