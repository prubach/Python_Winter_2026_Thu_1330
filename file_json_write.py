from csv_read_rates import csv_to_pandas
import json

my_json_file = 'data/rates.json'

dict_rates = csv_to_pandas('data/rates.csv', 1)

with open(my_json_file, 'w') as json_file:
    json.dump(dict_rates, json_file)

