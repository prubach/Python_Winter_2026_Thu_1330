for a in range(10):
    print(a, end=' ')

print('\n' + '-'*60)

for a in range(3, 10):
    print(a, end=' ')

print('\n' + '-'*60)

for a in reversed(range(3, 10)):
    print(a, end=' ')

print('\n' + '-'*60)

for a in range(20, 50, 3):
    print(a, end=' ')

print('\n' + '-'*60)

for a in range(50, 30, -1):
    print(a, end=' ')

print('\n' + '-'*60)

for a in range(20, 50, 2):
    if a % 3 == 0:
        print('?', end=' ')
        continue
    print(a, end=' ')

