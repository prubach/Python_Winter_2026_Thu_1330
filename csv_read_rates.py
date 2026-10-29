#CSV_READER
import csv

def curr_cal(pln):
    my_file = 'data/rates.csv'
    dict_cur = {}
    cur_lst = []
    with open(my_file, 'r') as f:
        cur_lst = f.readlines()
        #for line in lines:
        #    cur_lst.append(line.strip())

        cur_lst = cur_lst[1:]
        cur_lst = [x.strip() for x in cur_lst]
        print(f"Currency rates from the file:\n{cur_lst}")

    for item in cur_lst:
        key, value = item.split(',')
        dict_cur[key] = round(float(value) * pln, 2)  # not rounding off is giving more decimal
        # values for a couple of values
    print(f"Currency value after applying the conversion rates:\n{dict_cur}")


def cur_calculator(file_name, pln):
    cur_con = {}
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # to skip the header
        csv_dict = dict(csv_reader)
        print(f"The exchange rates of the target currencies:\n{csv_dict}")

    for key, value in csv_dict.items():
        cur_con[key] = round(float(value) * pln, 2)

    print(f"The currency equivalent of {pln} pln:\n{cur_con}")


# Using Pandas:
import pandas as pd

def csv_to_pandas(file_name, pln):
    df = pd.read_csv(file_name)
    #print(df)
    df = df.set_index('Currency')
    #print(df)
    #df['Rate'] = df['Rate'] * pln
    #rates = df['Rate'].to_list()
    #rates_proc = [x*pln for x in rates]
    df['Rate'] = df['Rate'].apply(lambda x: x * pln)
    dict_rates = df['Rate'].to_dict()
    return dict_rates

    #df['brand'] = df['brand'] * pln
    #print(df)

if __name__ == '__main__':
    #csv_to_pandas('data/rates.csv', 5)
    #curr_cal(2)
    #cur_calculator('data/rates.csv', 5)

    # Lambda expressions
    fl = lambda x: x * 5
    a = 100
    b = fl(a)
    print(f"b = {b}")

    print(csv_to_pandas('data/rates.csv', 10))