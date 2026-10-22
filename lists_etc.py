a_a = [3, 5, 7.5, 9, 11]
print(a_a)
print(type(a_a))

a_a.append(10)
a_a.append(5)
print(a_a)
# Insert 4 as 2nd element
a_a.insert(1, 4)
print(a_a)
# remove by value
a_a.remove(5)
print(a_a)
print(a_a.index(5))
#print(a_a.(4574))
# remove at index=2
a_a.pop(2)
print(a_a)

a_b = a_a.copy()
#a_b = a_a
a_b.sort()
print(f'a_b={a_b}')
print(f'a_a={a_a}')

