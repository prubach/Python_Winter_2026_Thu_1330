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
    a1.withdraw(300)

    #exit(-100)
    print(b)
    # Add deposit and withdraw methods and show how they can be used
except BankException as e:
    print(e)
except InsufficientBalanceException as e:
    print(e)
except Exception as e:
    print('Serious error')
    print(e)
    raise e

print('---- end ----')
print(b)

#script.sh 2>&1