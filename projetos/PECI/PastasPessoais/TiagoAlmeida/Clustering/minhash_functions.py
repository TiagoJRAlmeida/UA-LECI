from datasketch import MinHash

def get_shingles(text, n=2):
    return [text[i:i+n] for i in range(len(text) - n + 1)]


def jaccard_similarity(m1, m2):
    return m1.jaccard(m2)


def get_minhash(text, shingles, num_perm=128):
    m = MinHash(num_perm=num_perm)
    for shingles in get_shingles(text, shingles):
        m.update(shingles.encode('utf8'))
    return m