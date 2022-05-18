import AAFunks
import sqlite3
import AAClasses

login_user_data = sqlite3.connect("login_database.db")
cursor = login_user_data.cursor()

cursor.execute("SELECT username, email FROM login_user")
data_username = cursor.fetchall()

logining = True

while logining:
    user_1 = input("Prihlasovacie meno alebo email: ")
    user = AAClasses.User(user_1)

    if user_1 == user.nick or user.email:
        heslo = input("Zadajte heslo: ")
        login = AAFunks.log_in(user.password, heslo, 3)

        if login:
            print(f"Dobrý deň ", user.name)
            logining = False
            # pridať presmerovanie na uvodný_screen další.py

    else:
        print("Zlé prihlasovacie meno !")
        continue

# pre login vytvoríme ChildClass kde sa človek po zaregistrovaní može prihlasiť naserver ako
# uživaťeľ ale aj ako admin kde stránky už budu mať rozdielnu funkcionalitu admin bdue vytvárať
# uživateľske rozhranie a a uživateľ samozrejme použivať to rozhranie
