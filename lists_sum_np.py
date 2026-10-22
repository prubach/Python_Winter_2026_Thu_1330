import numpy as np

arr_a = [[1, 4, 6], [6, 9, 3], [2, 7, 9]]
print(f'arr_a={arr_a}')
a = [1, 4, 6]
b = [6, 9, 3]
c = [2, 7, 9]
arr_b = [a, b, c]
print(f'arr_b={arr_b}')
arr_c = arr_a + arr_b
print(f'arr_c={arr_c}')

sum_rows = np.sum(arr_a, axis=1)
print(f'sum_rows={sum_rows}')
print(f'type(sum_rows)={type(sum_rows)}')
sum_rows_list = list(sum_rows)
print(f'sum_rows_list={sum_rows_list}')
sum_rows_list = [int(x) for x in sum_rows_list]
print(f'sum_rows_list={sum_rows_list}')

sum_cols = np.sum(arr_a, axis=0)
print(f'sum_cols={sum_cols}')

print(np.iinfo(np.int64))