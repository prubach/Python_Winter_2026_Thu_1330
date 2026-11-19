from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100))
    last_name = Column(String)
    email = Column(String(200))
    accounts = relationship('Account', back_populates='customer')
    bank = relationship('Bank', lazy='select', back_populates='customers')
    fk_bank_id = Column(Integer, ForeignKey('bank.id'), nullable=False)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"C({self.id}, {self.first_name}, {self.last_name})"

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float)
    currency = Column(String)
    customer = relationship(Customer, back_populates='accounts')
    fk_customer_id = Column(Integer, ForeignKey('customer.id'))
    bank = relationship('Bank', lazy='select', back_populates='accounts')
    fk_bank_id = Column(Integer, ForeignKey('bank.id'), nullable=False)

    yearly_interest_rate = Column(Float)

    def __init__(self, customer, currency='PLN'):
        self.customer = customer
        self._balance = 0
        self.currency = currency

    def deposit(account, amount):
        # TODO - as part of the home assignment please extend this method
        account._balance += amount
        print(f"Deposited {amount} to {account}")

    def balance(account):
        return account._balance

    # code for creating withdraw method
    def withdraw(account, amount):
        # TODO - as part of the home assignment please extend this method
        if amount <= 0:
            raise InvalidAmountException(f"Withdrawal amount {amount} is negative")

        if account._balance >= amount:
            account._balance -= amount
            print(f"Withdrew {amount} from {account}")
        else:
            #p = 5546 + 'fsdfg'
            raise InsufficientBalanceException(f'Insufficient balance to withdraw: {amount}', amount, account._balance)

    def __repr__(self):
        return f"A({self.id}, {self.customer.last_name}, {self._balance} {self.currency})"


class Bank(Base):
    __tablename__ = 'bank'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    customers = relationship(Customer)
    accounts = relationship(Account)

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
    def __init__(self, message, amount_requested, amount_available):
        super().__init__(message)
        self.amount_requested = amount_requested
        self.amount_available = amount_available


class InvalidAmountException(BankException):
    pass


class DBSession:
    current_db_session = None

    def engine(self):
        url = 'sqlite:///data/bank.db'
        return create_engine(url, echo=True)

    def db_session(self):
        if not DBSession.current_db_session:
            Session = sessionmaker(bind=self.engine(), autoflush=False, autocommit=False)
            current_db_session = Session()
        return current_db_session

def init_db():
    db_session = DBSession()
    Base.metadata.create_all(bind=db_session.engine())