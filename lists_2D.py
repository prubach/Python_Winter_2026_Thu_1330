arr_a = [[1, 4, 6], [6, 9, 3], [2, 7, 9]]
print(f'arr_a={arr_a}')
a = [1, 4, 6]
b = [6, 9, 3]
c = [2, 7, 9]
arr_b = [a, b, c]
print(f'arr_b={arr_b}')
arr_c = arr_a + arr_b
print(f'arr_c={arr_c}')

print(arr_a[2])
print(arr_a[2][2])

# def sum_rows(arr):
#     # return a list with sums of each row in arr
#
# def sum_cols(arr):
#     # return a list with sums of each column in arr
#
# def sum_all(arr):
#     # return sum of all elements of arr

def sum_rows(arr):
    row_sums = [0] * len(arr)
    for i in range(len(arr)):
        row_sums[i] = sum(arr[i])
    return row_sums

    # return a list with summ of each column

def sum_rows_sl(arr):
    return [sum(row) for row in arr]


def sum_col(arr):
    num_cols = len(arr[0])
    col_sums = [0] * num_cols
    for row in arr:
        for j in range(num_cols):
            col_sums[j] += row[j]

    return col_sums

def sum_col_sl(arr):
    print(f'zip(*arr)={list(zip(*arr))}')
    return [sum(x) for x in zip(*arr)]


# return a sum of all elements in an array

# def sum_all(arr):
#     total_sum = 0
#     for row in arr:
#         total_sum += sum(row)
#     return total_sum

def sum_all(arr):
    return sum(sum_col(arr))

print(f'sum_rows={sum_rows(arr_a)}')
print(f'sum_rows_sl={sum_rows_sl(arr_a)}')
print(f'sum_col={sum_col(arr_b)}')
print(f'sum_col_sl={sum_col_sl(arr_b)}')
print(f'sum_all={sum_all(arr_b)}')

a = [1, 3, 5, 6]
b = [x*x for x in a if x > 4]

print(f'a={a}')
print(f'b={b}')

c = 100 if a[1] > 4 else 0
print(f'c={c}')

print('-' * 60)

l_a = [1, 5, 7]
l_b = [2, 4, 6]
print(f'l_a={l_a}')
print(f'l_b={l_b}')
# Zip - merge elements from 2 lists
l_c = list(zip(l_a, l_b))
print(f'l_c={l_c}')
# * - Unzip
l_d = list(zip(*l_c))
print(f'l_d={l_d}')

print(f'l_a\'={l_d[0]}')
print(f'l_b\'={l_d[1]}')
