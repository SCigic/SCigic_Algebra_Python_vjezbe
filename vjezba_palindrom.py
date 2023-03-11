word = input(f"Unesite rijec:  ").lower()

reversed_word = ""

for i in reversed(word): 
    reversed_word += i

# word[::-1]
# reversed_word == reversed(word) ne može 

if word == reversed_word: 
    print("Palindrom")
else: 
    print("Nije palindrom")

print(word[::-1])

