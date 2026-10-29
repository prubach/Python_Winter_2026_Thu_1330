import json

my_json_file = 'data/rates.json'

with open(my_json_file) as f:
    dict_rates = json.load(f)

print(dict_rates)
for key, value in dict_rates.items():
    print(key, value)
    print(type(key), type(value))