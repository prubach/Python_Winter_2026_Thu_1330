from typing import TypedDict

#list_a = [3, 5, 7.5, 9, 11]
list_a = [25, 5, 7.5, 9, 25, 7.5, 11, 25, 5]
print(list_a)
print(type(list_a))
tuple_a = (3, 5, 7.5, 9, 11)
print(tuple_a)
print(type(tuple_a))
print(tuple_a[3])

# Tuples can't be changed - immutable
#tuple_a.append(4)
#tuple_a.remove(3)
#tuple_a.sort()
#tuple_a[3] = 25

print('-'*60)

# Unordered and no duplicates = unique values
set_a = set(list_a)
print(set_a)
print(type(set_a))

#print(set_a[2])
set_a.add(3.5)
print(set_a)

list_b = list( set(list_a))
print(list_b)