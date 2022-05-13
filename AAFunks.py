import random

def add_into_list(database, in_put):
    if in_put not in database:
        database.append(in_put)
        return database
    else:
        if in_put in database:
            return True


def remove_from_list(database, in_put):
    if in_put in database:
        database.remove(in_put)
        return database
    else:
        return False


def print_under(data):
    for jednotku in data:
        print(jednotku)


def compare_list_data(name_list, data):
    if data in name_list:
        return True


def translate(phrase, string, string2):  # call = print(translate())
    translation = ""                     # paramet1=string ktorý ideme zmeniť
    for letter in phrase:                # paramet2=ktorý ma nahradiť
        if letter in string:             # paramet3=ktorým ideme nahradiť
            translation = translation + string2
        else:
            translation = translation + letter
    return translation


def check_phrase(phrase, pole):
    for jednotka in phrase:
        if jednotka in pole:
            return True

def dnajw(phrase, pole):
    counter = 0
    for jednotka in phrase:
        if jednotka in pole:
            counter += 1
    if counter >= 1:
        return True
    else:
        return False

def list_into_tuple(database):
    return tuple(database)


def string_na_pole(string):
    pole = []
    for letter in string:
        pole.append(letter)
    return pole


def log_in(password, in_put, in_put_limit):
    in_put_count: int = 0                # in_put=zadané heslo od uživateľa
    in_put_limit: int                    # vracia boolien podľa vysledku
    zoznam = False
    while in_put != password and not zoznam:
        if in_put_count < in_put_limit:
            in_put = input("Zadajte heslo!: ")
            in_put_count += 1
        else:
            zoznam = True
    if zoznam:
        print("Wrong Password")
        return not zoznam
    elif in_put == password:
        print("Vitajte!")
        return not zoznam


def trans(phrase):  # call = print(translate())
    translation = ""
    rad1 = ["+", "ľ", "š", "č", "ť","ž", "ý", "á", "í", "é"]
    rad2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for letter in phrase:
        if letter in rad1[0]:
            translation = translation + str(rad2[0])
        elif letter in rad1[1]:
            translation = translation + str(rad2[1])
        elif letter in rad1[2]:
            translation = translation + str(rad2[2])
        elif letter in rad1[3]:
            translation = translation + str(rad2[3])
        elif letter in rad1[4]:
            translation = translation + str(rad2[4])
        elif letter in rad1[5]:
            translation = translation + str(rad2[5])
        elif letter in rad1[6]:
            translation = translation + str(rad2[6])
        elif letter in rad1[7]:
            translation = translation + str(rad2[7])
        elif letter in rad1[8]:
            translation = translation + str(rad2[8])
        elif letter in rad1[9]:
            translation = translation + str(rad2[9])
        else:
            translation = translation + letter
    return translation


def user_num(database):
    num = ()
    if num not in database:
        num = random.random()
        return num

