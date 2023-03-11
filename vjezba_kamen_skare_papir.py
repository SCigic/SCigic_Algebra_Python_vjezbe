import random 
import os

ksp_dict = {
    1: "kamen",
    2: "skare",
    3: "papir"
}

while True: 

    rand_int = random.randint(1,3)
    ksp_value = ksp_dict[rand_int]

    user_pick = input("Unesite kamen/skare/papir: ")

    if user_pick.lower() in ksp_dict.values():
        if user_pick.lower() == ksp_value:
            print(f"Nerjeseno. Oboje ste odabrali: {ksp_value}. Pokusajte ponovno. ")
        elif user_pick.lower() == "skare":
            if ksp_value == "papir":
                print(f"{ksp_value}! Pobijedili ste!")
            else:
                print(f"{ksp_value}! Izgubili ste!")
        elif user_pick.lower() == "papir":
            if ksp_value == "skare":
                print(f"{ksp_value}! Izgubili ste!")
            else:
                print(f"{ksp_value}! Pobijedili ste!")
        else:
            if ksp_value == "skare":
                print(f"{ksp_value}! Pobijedili ste!")
            else:
                print(f"{ksp_value}! Izgubili ste!")       
    else: 
        print("Unesite jednu od ponuđenih riječi!")
        continue

    play_again = input("Zelite li igrati ponovno (Y/N): ")

    if play_again == "N": 
        break
    else:
        os.system("cls")




