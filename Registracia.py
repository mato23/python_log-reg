import AAFunks
import sqlite3
import random

# začnem písať backend pomyselnej prvej strany webu
# funkcionalita registracie kde uživaťeľ vypíše formular ako pri reg.

# na začiatok skusim napísať klasu uživateľa a funkciu
# ktorá mi bude generovať nahodne čislo pod ktoré sa uloží užívateľ dalej superklasu admina

login_user_data = sqlite3.connect("login_database.db")
cursor = login_user_data.cursor()

# cursor.execute("""create table login_user (
#    user_number integer,
#    username text,
#    password text
#    first_name text,
#    last_name text,
#    email text,
#    phone_number integer
#    )""")

registration = []

create = True
while create:
    user_num = random.randint(1, 9999)
    if user_num not in cursor.execute("select user_number from login_user"):
        registration.append(int(user_num))
        create = False
    else:
        continue

create = True
while create:
    username = input("Username: ")
    database = cursor.execute("select username from login_user")
    cursor.fetchone()
    if username in database:
        print("Username už existuje.")
        continue
    else:
        registration.append(username)
        create = False


create = True
while create:
    password = input("Zadajte heslo: ")
    password_2 = input("Zadajte heslo znova: ")
    cisla = [0, 1, 2, 3, 4, 5, 7, 8, 9]
    if password != password_2:
        print("Heslo sa nezhoduje !")
        continue
    elif not AAFunks.check_phrase(password, str(cisla)):
        print("Heslo musí obsahovať najmenej jedno číslo !")
        continue
    elif len(password) <= 5:
        print("Musí obsahovať najmenej 6 znakov !")
    else:
        registration.append(password)
        create = False

name = input("Vaše meno: ")
surname = input("Vaše priezvisko: ")
name_surname = name.replace(name[0], name[0].upper()) + " " + surname.replace(surname[0], surname[0].upper())
registration.append(str(name_surname))

email = input("Vaša emailová adresa: ")
registration.append(str(email))

tel_num = input("Vaše tel. číslo: ")
registration.append(int(tel_num))


registration1 = [AAFunks.list_into_tuple(registration)]


cursor.executemany("insert into login_user values(?,?,?,?,?,?)", registration1)

login_user_data.commit()
login_user_data.close()
