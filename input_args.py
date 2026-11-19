
import sys

from bank import Bank

args = sys.argv
print(args)

bank_name = args[1] if len(args) > 1 else 'My Bank'

b = Bank(bank_name)
c1 = b.create_customer('John', 'Smith')
c2 = b.create_customer('Anne', 'Brown')
a1 = b.create_account(c1, 'USD')
a2 = b.create_account(c2, 'USD')
a3 = b.create_account(c1, 'USD')
a4 = b.create_account(c2, 'USD')
print(b)