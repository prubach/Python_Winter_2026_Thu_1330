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
    if a > 40:
        print('aborting for loop')
        break
    print(a, end=' ')

print('\n' + '-'*60)

i = 0
while i < 10:
    print(i, end=' ')
    i += 1