import sqlite3
import AAFunks

login_user_data = sqlite3.connect("login_database.db")
cursor = login_user_data.cursor()

class User:
    def __init__(self, nick):
        cursor.execute("SELECT * FROM login_user ORDER BY user_number")
        for row in cursor.fetchall():
            if nick in row:
                if nick == row[1]:
                    self.nick = row[1]
                    self.num = row[0]
                    self.name = row[3]
                    self. password = row[2]
                    self.email = row[4]
                    self.tel_num = row[5]



    def print_data(self):
        print(self.email)
        print(self.num)
        print(self.name)



matko = User("martinez")

matko.print_data()
