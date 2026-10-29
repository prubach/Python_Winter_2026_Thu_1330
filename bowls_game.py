'''
 * * * * *
  * * * *
   * * *
    * *
     *

n - number of rows, above n=5
'''

def count_bowls_sum_list(n):
    # compute how many bowls we have altogether given the number of rows n
    bucket = list(range(n, 0, -1))
    sum_of_bowls = sum(bucket)
    return sum_of_bowls


def count_bowls_from_file():
    my_file = 'data/test.txt'

    f = open(my_file)
    lines = f.readlines()
    sum = 0
    print(lines)
    for line in lines:
        line = line.strip()
        ct = len(line)
        sum = sum + ct
        # print(line, end='')
    f.close()
    return sum

n = 5
print(f'count_bowls_sum_list: {count_bowls_sum_list(n)}')
print(f'count_bowls_from_file: {count_bowls_from_file()}')