class Customer:
    last_id = 0
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Customer.last_id = Customer.last_id + 1
        self.id = Customer.last_id

    def __repr__(self):
        return f"C({self.id}, {self.first_name}, {self.last_name})"

class Account:
    last_id = 1000
    yearly_interest_rate = 0.02  # TODO - will be used to update the interest rate

    def __init__(self, customer, currency='PLN'):
        self.customer = customer
        self._balance = 0
        Account.last_id += 1
        self.id = Account.last_id
        self.currency = currency

    def deposit(account, amount):
        # TODO - as part of the home assignment please extend this method
        account._balance += amount
        print(f"Deposited {amount} to {account}")

    # code for creating withdraw method
    def withdraw(account, amount):
        # TODO - as part of the home assignment please extend this method
        if account._balance >= amount:
            account._balance -= amount
            print(f"Withdrew {amount} from {account}")
        else:
            p = 5546 + 'fsdfg'
            raise InsufficientBalanceException(f'Insufficient balance to withdraw: {amount}')
            print("Insufficient funds")

    def __repr__(self):
        return f"A({self.id}, {self.customer.last_name}, {self._balance} {self.currency})"


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.accounts = []

    def create_customer(self, first_name, last_name):
        customer = Customer(first_name, last_name)
        self.customers.append(customer)
        return customer

    def create_account(self, customer, currency = 'PLN'):
        account = Account(customer, currency)
        self.accounts.append(account)
        return account

    def transfer_money(self, from_account_id, to_account_id, amount):
        # TODO - as part of the home assignment please implement this method - as names suggest the input parameters are
        # ids of the accounts to transfer money from and to and amount to transfer. You may need a helper method to find
        # those accounts based on their ids.
        pass

    def run_daily_interest_updater(self):
        # TODO - as part of the home assignment please implement this method
        pass

    def __repr__(self):
        return f"B({self.name}, \n{self.customers}, \n{self.accounts})"

class BankException(Exception):
    pass

class InsufficientBalanceException(BankException):
    pass