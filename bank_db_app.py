from bank_models import Bank, Account, Customer, init_db, DBSession

db = DBSession().db_session()

init_db()
