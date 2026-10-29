from csv_read_rates import csv_to_pandas
import pickle

my_pkl_file = 'data/rates.pkl'

dict_rates = csv_to_pandas('data/rates.csv', 1)

with open(my_pkl_file, 'wb') as pkl_file:
    pickle.dump(dict_rates, pkl_file)

