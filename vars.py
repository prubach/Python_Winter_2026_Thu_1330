i_a = 41234
i_b = 42563
i_c = i_a + i_b
type_i_c = type(i_c)
print(f'type_i_c: {type_i_c} i_c = {i_c}')

i_d = 3672396796732607390692456182642659821658926158962587265981265126759821659128652198561298562521512
i_e = 1545482658265826582465892659823656591865982167598271658217658742659812675182659821659218651286519
i_f = i_d * i_e
print(f'i_f: {i_f}')
s_f = str(i_f)
s_f = s_f + '0000000'
print(f'type(s_f): {type(s_f)}')
print(f's_f: {s_f}')
print(f'len(s_f): {len(s_f)}')
i_g = int(s_f)
print(f'type(i_g): {type(i_g)}')
print(f'i_g: {i_g}')

f_a = 252.34536
print(f'type(f_a): {type(f_a)}')
print(f'f_a: {f_a}')

print('------------------------')
'''
These are int and float operations

'''
f_d = float(i_d)
# f_d = 3672396796732607390692456182642659821658926158962587265981265126759821659128652198561298562521512.0
f_e = 1545482658265826582465892659823656591865982167598271658217658742659812675182659821659218651286519.0
f_f = f_d * f_e
print(f'f_f: {f_f}')
import sys
print(sys.float_info)
print(sys.int_info)

bi_a = 0b11010
print(f'type(bi_a): {type(bi_a)}')
print(f'bi_a: {bi_a}')

hi_a = 0x2b
print(f'hi_a: {hi_a}')

a = 10
b = 30
# power
c = (a + b)**5
print(c)

d = b % 4
print(d)

print('--------------')
s_a = '4.252535235e2'
print(f'type(s_a): {type(s_a)}')
print(f's_a: {s_a}')
i_a = float(s_a)
print(f'type(i_a): {type(i_a)}')
print(f'i_a: {i_a}')
