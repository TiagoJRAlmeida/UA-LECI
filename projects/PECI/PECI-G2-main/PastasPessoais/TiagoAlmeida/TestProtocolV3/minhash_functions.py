from datasketch import MinHash


# NOTE: This function is not used in the current version of the code because minhash is not currently being used.
# For more information check the NOTE above the function "correct_name_without_standard()" in the main file.
def get_shingles(text, n=2):
    return [text[i:i+n] for i in range(len(text) - n + 1)]


# NOTE: This function is not used in the current version of the code because minhash is not currently being used.
# For more information check the NOTE above the function "correct_name_without_standard()" in the main file.
def jaccard_similarity(m1, m2):
    return m1.jaccard(m2)


# NOTE: This function is not used in the current version of the code because minhash is not currently being used.
# For more information check the NOTE above the function "correct_name_without_standard()" in the main file.
def get_minhash(text, num_perm=128):
    m = MinHash(num_perm=num_perm)
    for shingles in get_shingles(text):
        m.update(shingles.encode('utf8'))
    return m