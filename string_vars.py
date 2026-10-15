s_1 = 'abcdef'
s_2 = 'ghijkl'
print(f's_1: {s_1}')
print(f's_2: {s_2}')
s_3 = s_1 + s_2
print(f's_3: {s_3}')
s_4 = s_3[2:5]
print(f's_4: {s_4}')

s_5 = 'A'
print(ord(s_5))
print(chr(113))

s_6 = 'abc\ndef\r\nghijkl\tgfwegw\t\tshsh'
print(f's_6: {s_6}')
s_7 = 'abc\\ndef\r\nghijkl\tgfwegw\t\tshsh'
# raw string
s_7 = r'abc\ndef\r\nghijkl\tgfwegw\t\tshsh'
print(f's_7: {s_7}')

s9 = "abc'ed'"
s9 = 'abc"ed"'
s9 = 'abc\'ed\''
print(f's9: {s9}')

s10 = 'ż'
print(ord(s10))

pos_def = s_7.find('shethh')
# if nto found casues ValueError
pos_def = s_7.index('sh')
print(f'pos_def: {pos_def}')
pos_def = s_7.rfind('sh')
print(f'pos_def: {pos_def}')