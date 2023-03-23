# izbornik
# otvaranje računa
# prikaz stanja računa
# prikaz prometa po računu
# polog novaca na račun
# podizanje novaca s računa
# izlazak iz programa (povratak na main menu)

import os
import random

def menu():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print("\t1. Otvaranje racuna")
    print("\t2. Prikaz stanja racuna")
    print("\t3. Prikaz prometa po racunu")
    print("\t4. Polog novca na racun")
    print("\t5. Podizanje novca s racuna")
    print()


def account_opening(company_name):
    account_number = random.randint(1000100010001000,9999999999999999)
    bank_accounts.update({account_number:[company_name,0]})

bank_accounts = {} #{account_number : [company_name, account_balance]}

bank_account = {
    "account_number" : "29182736", 
    "account_holder" : {
        "first_name":"Pero",
        "last_name":"Peric",
    }
    "account_balance": 4_789_000
}

while True: 
    menu()
    user_selection = int(input("Izaberite akciju 1-5: "))
    if user_selection == 1: 
        pass
        #account_opening(company_name)
    elif user_selection == 2:
        pass 
    elif user_selection == 3:
        pass 
    elif user_selection == 4:
        pass 
    elif user_selection == 5:
        pass 