import random

tal = random.randint(1,100)

AnvandaresGissning = int(input("Gissa talet: "))
Raknare = 1

while AnvandaresGissning != tal:
    if AnvandaresGissning > tal:
        print("Mindre!")
    else:
        print("Större!")

    AnvandaresGissning = int(input("Gissa talet igen: "))
    Raknare += 1

print("Korrekt! Antal försök: ", Raknare)