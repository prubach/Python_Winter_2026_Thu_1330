import os
my_file = os.path.join('data', 'hello_out.txt')

# mode:
# w - overwrite
# a - append to existing file
with open(my_file, 'w') as f:
    f.write('hello world\n')
    f.write('this is python\n')
    f.flush()
    f.write('SGH\n')


