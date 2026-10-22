import os
my_file = 'data/hello.txt'
my_file = 'data\\hello.txt'
my_file = r'data\hello.txt'
my_file = os.path.join('data', 'hello.txt')

f = open(my_file)
lines = f.readlines()
print(lines)
for line in lines:
    print(line, end='')
f.close()

print('\n' + '-' * 60)

with open(my_file, 'r') as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line, end='')

print('\n' + '-' * 60)