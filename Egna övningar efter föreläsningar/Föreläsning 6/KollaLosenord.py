KorrektLosenord = "Hej"

AnvandareLosenord = input("Lösenord:")

while AnvandareLosenord != KorrektLosenord:
    AnvandareLosenord = input("Det var inte korrekt lösenord. Var god försök igen: ")

print("Du är inloggad!")