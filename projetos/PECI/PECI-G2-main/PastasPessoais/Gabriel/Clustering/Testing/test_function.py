from strings_manipulation import * 
from minhash_functions import *
from remove_commonwords import remove_common
import json

w1 = "ETE-LOGIATICA,SAAV. INFANTE SANTO 2H 2 PISO"
w2 = "ETE - Log\u00edstica, S.A"

print(remove_common(w1))
print(remove_common(w2))

m1 = get_minhash(remove_common(w1))
m2 = get_minhash(remove_common(w2))

print(jaccard_similarity(m1,m2))

with open("part_count.json","r") as file:
        word_count = json.loads(file.read())

word_count = {k:word_count[k] for k in sorted({i for i in word_count.keys()})}

with open("part_count.json","w") as file:
        json.dump(word_count,file,indent=6)