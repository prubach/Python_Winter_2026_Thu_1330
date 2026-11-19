from bank import Customer, Account, Bank, InsufficientBalanceException, BankException

b = Bank('SGH Bank')
c1 = b.create_customer('John', 'Smith')
c2 = b.create_customer('Anne', 'Brown')
a1 = b.create_account(c1, 'USD')
a2 = b.create_account(c2, 'USD')
a3 = b.create_account(c1, 'USD')
a4 = b.create_account(c2, 'USD')
print(b)


try:
    a1.deposit(200)
    # a = 1225
    # b = '2525'
    # c = a + b
    print('You have: {}'.format(a1.balance()))
    withdraw_amount_str = input('Enter withdraw amount: ')
    withdraw_amount = float(withdraw_amount_str)
    a1.withdraw(withdraw_amount)
    #exit(-100)
    print(b)
    # Add deposit and withdraw methods and show how they can be used
except InsufficientBalanceException as e:
    print(e)
    req_am = e.amount_requested
    ava_am = e.amount_available
    print('Requested/Available: {}/{}'.format(req_am, ava_am))
except BankException as e:
    print(e)
except Exception as e:  # Use with caution as it may hide all bugs
    print('Serious error')
    print(e)
    raise e

print('---- end ----')
print(b)

#script.sh 2>&1