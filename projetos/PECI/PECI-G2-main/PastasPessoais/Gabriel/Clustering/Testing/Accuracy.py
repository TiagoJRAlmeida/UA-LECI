import json

with open("test_data.json","r") as f:
    test = json.loads(f.read())

with open("train_data.json","r") as f:
    train = json.loads(f.read())

total = len({j for i in test.values() for j in i})

count = 0

for i in test.keys():
    count += len(set(train[i]["names"]) & set(test[i]))

print(f"Accuracy : {(count/total)*100}")