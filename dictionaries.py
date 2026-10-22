dict_a = {'PLN': 1, 'USD': 3.7, 'EUR': 4.3}
print(dict_a)

print(dict_a['EUR'])
#print(dict_a['GBP'])  # KeyError
print(dict_a.get('USD'))
print(dict_a.get('GBP'))

#if 'GBP' in dict_a.keys():
#if dict_a.get('GBP') != None:
if dict_a.get('GBP'):
    print(dict_a['GBP'])
else:
    print('no GBP in dictionary')

print(dict_a.get('GBP', 5.0))


