a_a = [3, 5, 7.5, 9, 11]
print(a_a)
print(type(a_a))
# Element #2 = 5
print(a_a[1])
print(type(a_a[1]))

a_b = a_a[1:4]
print(a_b)

a_b = a_a[1:]
print(a_b)

a_b = a_a[:4]
print(a_b)

a_b = a_a[-2:]
print(a_b)

print(len(a_a))
print('------------------------')
sum_a_a = 0
for a in a_a:
    print(f'a={a} type: {type(a)}')
    sum_a_a += a  # sum_a_a = sum_a_a + a
print(f'a={a}')
print(f'sum_a_a: {sum_a_a}')