s = 'AB'

match s:
    case 'A':
        print('s=A')
    case 'B':
        print('s=B')
    case 'ABC':
        print('s=ABC')
    case _:  # default case
        print('s not {A,B,ABC}')
