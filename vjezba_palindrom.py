word = input(f"Unesite rijec:  ").lower()

reversed_word = ""

for i in reversed(word): 
    reversed_word += i

if word == reversed_word: 
    print("Palindrom")
else: 
    print("Nije palindrom")

