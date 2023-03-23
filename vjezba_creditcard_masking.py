# napisi program koji će sve znakove osim zadnja 4 maskirati pomoću ####
# ako je korisnik unio "-", onda se ti znakovi ne zaštićuju
# neka korisnik bira kojim će znakom zaštititi karticu
# 2349-9281-9283-1029

import os

os.system("cls")

card_number = input("Unesite broj kreditne kartice: ")
mask_symbol = input("Kojim simbolom želite maskirati brojeve: ")


def check_format(card:str):
    if len(card) not in [16,19]: 
        return 3
    elif len(card) == 19: 
        if (card[4] and card[9] and card[14]) =="-":
            return 1
        else: 
            return False
    else: 
        return 2


while True: 

    if check_format(card=card_number) == 1: # 2349-9281-9283-1029
        masked_card = ""
        for i,n in enumerate(card_number): 
            if i not in [4, 9, 14, 15, 16, 17, 18, 19]:
                masked_card += mask_symbol
            else: 
                masked_card += card_number[i]
        print(masked_card)
        break

    elif check_format(card=card_number) == 2: # 2349928192831029
        masked_card = ""
        for i,n in enumerate(card_number): 
            if i not in [12, 13, 14, 15]:
                masked_card += mask_symbol
            else: 
                masked_card += card_number[i]
        print(masked_card)
        break

    elif check_format(card=card_number) == 3:
        print(f"Unijeli ste {len(card_number)} brojeva, a trebali ste 14")
        break