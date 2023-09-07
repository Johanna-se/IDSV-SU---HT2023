anvandarnamn = input("Skriv ditt användarnamn: ")
losenord = input("Lösenord: ")

if (anvandarnamn == "admin") and (losenord == "password123"):
    print ("Inloggning lyckades")
else:
    print("Inloggning misslyckades")