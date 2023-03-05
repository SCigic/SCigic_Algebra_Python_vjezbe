import os

chosen_phrase = input(f"Unesite zadani izraz: ").lower()
os.system("cls")
letter_tracker = []
mistakes = 0


for i in chosen_phrase:
    if i == " ": 
        print(" ", end = " ")
    else:
        print("_", end = " ")

print()
print()

def print_vjesala(m): 
    if m == 1: 
        print(" __")
        print("|  |")
        print("|  O")
        print("| ")
        print("| ")
    if m == 2: 
        print(" __")
        print("|  |")
        print("|  O")
        print("|  |")
        print("|  ")
    if m == 3: 
        print(" __")
        print("|  |")
        print("|  O")
        print("|  |\\")
        print("|  ")
    if m == 4: 
        print(" __")
        print("|  |")
        print("|  O")
        print("|  /|\\")
        print("|  ")
   
    if m == 5: 
        print(" __")
        print("|  |")
        print("|  O")
        print("|  /|\\")
        print("|   \\")
    if m == 6: 
        print(" __")
        print("|  |")
        print("|  O")
        print("|  /|\\")
        print("|   /\\")


while mistakes < 6: 
    chosen_letter = input(f"\n\nOdaberite jedno slovo: ").lower()
    
    if chosen_letter in chosen_phrase: 
        if letter_tracker.count(chosen_letter) == 0:
            letter_tracker.append(chosen_letter)
        else:
            print("To ste slovo vec odabrali.")

    if set(letter_tracker) == set(chosen_phrase):
        print("---------------")
        print("Pobjeda! Bravo!")
        print("---------------")
        print(f"Ukupan broj pogresaka: {mistakes}/6")
        break


    if chosen_letter in letter_tracker:
        for i in chosen_phrase:
            if i in letter_tracker: 
                print( i , end = " ")
            elif i == " ": 
                print(" ", end = " ")
                letter_tracker.append(i)
            else:
                print("_", end = " ")
    else: 
        mistakes += 1
        print_vjesala(mistakes)
        print(f"Pogreska broj {mistakes}/6")
        if mistakes == 6: 
            print(f"Igra je zavrsena. Pokusajte ponovno.")
            print()
    
    