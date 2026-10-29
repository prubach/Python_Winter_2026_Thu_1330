from time import time

from bowls_game import *

def time_func(func, n):
    print(f'Running: {func.__name__}({n})')
    t0 = time()
    res = func(n)
    t1 = time()
    elapsed_time = round(t1 - t0, 8)
    print(f'Result: {res} Elapsed time: {elapsed_time}s')

n = 900

time_func(count_bowls_recursive, n)
time_func(count_bowls_sum_list, n)
time_func(count_bowls_sum, n)
time_func(count_bowls_sequence, n)
#time_func(count_bowls_from_file, n)