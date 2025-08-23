from datasketch import MinHash
from minhash_functions import *
from strings_manipulation import *
from remove_commonwords import remove_common

l1 = "DSV AIR & SEA INTERNATIONAL, S.L.U. (VIGO)"
l2 = "DSV AIR & SEA INTERNATIONAL, S.L.U. VIGO"

sim = dict()

sim[l1] = get_minhash(remove_common(l1))
sim[l2] = get_minhash(remove_common(l2))

m1 = get_minhash(remove_common(l1))
m2 = get_minhash(remove_common(l1))

print(jaccard_similarity(m1,m2))
print(jaccard_similarity(sim[l1],sim[l2]))