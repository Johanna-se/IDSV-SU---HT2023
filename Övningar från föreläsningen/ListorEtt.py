talen = []

tal = int(input("Tal: "))
while tal >= 0:
    talen += [tal]  #Slår ihop två listor, bättre metod för att göra detta kommer på nästa föreläsning
    tal = int(input("Tal: "))

kom = input("Kommando: ")
while kom != "sluta":
    match kom:
        case "skriv":
            for nummer in talen:
                print(nummer, end = " ")    #kommandot end = " " gör att nästa siffra ej skrivs på en nya rad utan att det blir ett mellanslag istället (följt av nästa siffra i listan)
            print()                         #Byt rad efter for-loopen
        case "summa":
            summa = 0
            for nummer in talen:
                summa += nummer
            print("Summa =", summa)
        case "addera":                      
            pos = int(input("Position: "))
            if pos < 0 or pos >= len(talen):
                print("Fel position!")
            else:
                talet = int(input("Att addera: "))
                talen[pos] += talet
        case "sluta":
            pass                                #betyder att programmet hoppas över.
        case _:                                 #alla övriga (felaktiga)
            print("Fel kommando!")
            
    kom = input("Kommando: ")

print("Tack och välkommen åter!")