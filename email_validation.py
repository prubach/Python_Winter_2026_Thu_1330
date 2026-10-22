def check_if_valid_email_simple(email):
    is_valid = False

    if '@' in email:
        is_valid = True

    return is_valid


print(check_if_valid_email_simple('mp@gmail.com'))

print('----------------------------------------------------')


def check_if_valid_email (email):
    # Contributed by Bayu Angorro
    is_valid = False

    # assign email as string without blank at the end
    email = email.strip()

    # set up the email characteristics Username and domain. use @ to split the parts
    if email.count('@') == 1:
        parts = email.split('@')
        username = parts[0]
        domain = parts[1]
    else:
        return False
    # set the conditions
    #if email.count ('@') !=1:  #must have only 1 '@' symbol
    #    is_valid = False
    if username == "" or domain == "": #username or domain cannot be blank
        is_valid = False
    elif '.' not in domain: #domain must have '.'
        is_valid = False
    elif domain.startswith('.') or domain.endswith('.'): #the '.' cannot be at beginning or very end of domain part
        is_valid = False
    elif not email.isascii() :
        is_valid = False
    else:
        is_valid = True #if none of above parameters are violated then it is an email. voila!

    return is_valid

    # testing
a= 'ba159111@student.sgh.waw.pl'
b= 'bayuanggoro@ '
c= 'bayu_aa.yahoo.com'
d= 'by_you@@microsoft.com'
e= 'bayu@.live.com'
f= 'bayu_arko.anggoro@outlook.365.com '
g= 'b.a.y.u@kprm.gov.pl.'

print(f' is " {a} " a valid email address?', check_if_valid_email(a))
print(f' is " {b} " a valid email address?', check_if_valid_email(b))
print(f' is " {c} " a valid email address?', check_if_valid_email(c))
print(f' is " {d} " a valid email address?', check_if_valid_email(d))
print(f' is " {e} " a valid email address?', check_if_valid_email(e))
print(f' is " {f} " a valid email address?', check_if_valid_email(f))
print(f' is " {g} " a valid email address?', check_if_valid_email(g))