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

