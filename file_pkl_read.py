import pickle

my_pkl_file = 'data/rates.pkl'

with open(my_pkl_file, 'rb') as f:
    dict_rates = pickle.load(f)

print(dict_rates)
for key, value in dict_rates.items():
    print(key, value)
    print(type(key), type(value))