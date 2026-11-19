from bank_models import Bank, Account, Customer, init_db, DBSession

db = DBSession().db_session()
init_db()

def add_data():
    b = Bank('SGH Bank')
    db.add(b)
    c1 = b.create_customer('John', 'Smith')
    c2 = b.create_customer('Anne', 'Brown')
    db.add(c1)
    db.add(c2)
    a1 = b.create_account(c1, 'USD')
    a2 = b.create_account(c2, 'USD')
    a3 = b.create_account(c1, 'USD')
    a4 = b.create_account(c2, 'USD')
    db.add(a1)
    db.add(a2)
    db.add(a3)
    db.add(a4)
    db.commit()
    print(b)


def get_customers():
    customers = db.query(Customer).filter(Customer.last_name.like('Sm%')).all()
    for c in customers:
        print(c)
        c.email = 'smith@sgh'
        print(c.accounts)
    db.commit()



if __name__ == '__main__':
    #add_data()
    get_customers()
