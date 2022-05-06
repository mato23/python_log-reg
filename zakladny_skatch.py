import Funks



term1 = 22.4
term2 = 24.4
term3 = 26.4
term4 = 27.4
term5 = 3.5

list_terminov = [term1, term2, term3, term4, term5]

print(" Vlasy od Marušky Login ")

meno_1 = input("Zadajte svoje Meno: ")
meno_2 = input("      a Priezvisko: ")

print("Dobrý Deň " + meno_1.upper(), meno_2.upper() + "!")
print(meno_1.upper() + ", Naše voľné termíný sú: ")

Funks.print_under(list_terminov)

interpuk = ", :-"
bodka = "."
vybrany_term = input("Napíšte vybraný termín: ")
preklad_0 = Funks.translate(vybrany_term, interpuk, bodka)
preklad_vybrany_term =  [Funks.trans(preklad_0)]

potvrdenie_2 = True
otazka = input("Mysleli ste " + preklad_vybrany_term[0] + " ? Y/N : ")
while potvrdenie_2:
    if "Y" == str(otazka.upper()):
        potvrdenie_2 = False
    elif "N" == str(otazka.upper()):            # input limit dáme and boolpodobne ako v def login
        Funks.print_under(list_terminov)
        vybrany_term_2 = input("Napíšte znova vybraný termín: ")
        preklad_3 = Funks.translate(vybrany_term_2, interpuk, bodka)
        preklad_4 = Funks.trans(preklad_3)
        otazka = input("Mysleli ste " + preklad_4 + " ? Y/N : ")
        preklad_vybrany_term[0] = preklad_4
    else:
        print("Nespárvny input!")
        otazka = input("Mysleli ste " + preklad_2[0] + " ? Y/N : ")


data_bool = Funks.compare_list_data(list_terminov, float(preklad_vybrany_term[0]))

if not data_bool:
    print(" Vami zvolený termín " + str(preklad_vybrany_term[0]) + " nieje v zozname. Prosím zvolte si z "
                                                                   "dostupných termínov! Ďakujeme.")
else:
    print("Váš termín " + meno_1.upper() + " je " + str(preklad_vybrany_term[0]) + " Tešíme sa na vás!")
    Funks.remove_from_list(list_terminov, float(preklad_vybrany_term[0]))
print(list_terminov)

print("skušame git")
