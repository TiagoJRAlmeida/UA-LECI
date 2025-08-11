test_dict = {'Test': {'value': 1.0}, 'Hello': {'value': 1.0}}

print(test_dict["Hello"])

test_dict.pop("Hello")
print(test_dict)
test_dict["Hello"] = {'value': 1.0}
print(test_dict)

for key in test_dict:
    print(key)