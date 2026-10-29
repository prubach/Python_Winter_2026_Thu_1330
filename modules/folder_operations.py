import json
import os

#my_json_file = 'data/rates.json'
my_json_file = os.path.join('..', 'data','rates.json') # relative path
#my_json_file = 'c:\\Users\\prubac\\PycharmProjects\\Python_Winter_2026_Thu_1330\\data\\rates.json' # absolute path

cwd = os.getcwd()

print(f'current working dir: {cwd}')

with open(my_json_file) as f:
    dict_rates = json.load(f)

print(dict_rates)

folder_list = os.listdir(cwd)
print(f'folderlist: {folder_list}')
print(os.path.dirname(my_json_file))


my_data_folder = os.path.dirname(my_json_file)
folder_list = os.listdir(my_data_folder)
print(f'folderlist: {folder_list}')
for f in folder_list:
    size = os.stat(os.path.join(my_data_folder, f)).st_size
    print(f'{f}: {size}')

