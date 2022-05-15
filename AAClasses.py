import sqlite3

login_user_data = sqlite3.connect("login_database.db")
cursor = login_user_data.cursor()


class User:
    def __init__(self, nick):
        cursor.execute("SELECT * FROM login_user ORDER BY user_number")
        counter = 0
        for row in cursor.fetchall():
            if nick in row:
                counter += 1
                if nick == row[1] or row[4]:
                    self.nick = row[1]
                    self.num = row[0]
                    self.name = row[3]
                    self. password = row[2]
                    self.email = row[4]
                    self.tel_num = row[5]
            elif counter == 0:
                none = "none"
                self.nick = none
                self.num = none
                self.name = none
                self.password = none
                self.email = none
                self.tel_num = none

    def print_data(self):
        print("Meno a Priezvisko: ", self.name)
        print("Uživatelské číslo: ", self.num)
        print("Email: ", self.email)
        print("Telefónne číslo: ", self.tel_num)

    def show_password(self):
        print(self.password)
