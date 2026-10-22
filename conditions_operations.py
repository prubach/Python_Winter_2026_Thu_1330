p = False
q = True
print(f'p: {p}')
print(f'q: {q}')

if p and q:
    print('p and q are True')
else:
    print('p or q is False')

print('-'*60)

if p or q:
    print('p or q is True')
else:
    print('p and q are False')

print('-'*60)

# XOR
if p ^ q:
    print('p xor q is True')
else:
    print('p xor q is False')


