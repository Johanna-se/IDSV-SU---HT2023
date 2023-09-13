# Skriv ett Python-program som läser från användaren en lång textrad bestående av flera ord
# avdelade med mellanslag. Med ord här menas bara följder av icke-blanka tecken avslutade av
# mellanslag eller slutet på strängen. Dela upp den inlästa texten i ord.
# Programmet ska räkna hur många gånger varje ord förekommer i texten, och skriva ut en
# tabell med orden och deras förekomster.
# För detta kan man använda två listor: en med orden och en med heltal som ska fungera som
# räknare för motsvarande ord. Orden och räknarna bör ligga på samma position i var sin lista.
# Obs! att precis som i uppgift 2 finns det bättre lösningar på detta

#Be användaren om en mening
anvandresInput = input("Skriv en mening: ")

#Splitta meningen till en lista med ett ord på varje index
ordLista = anvandresInput.split()

#Skapa en tom lista för att räkna antal ord
antalOrdLista = []

#loopa igenom listan för att räkna
for ord in ordLista:
    antal = ordLista.count(ord)                 # Antalet förekomster av ord vilket är ett index

    #Lägg till antal i antalOrdListan
    antalOrdLista.append(antal)

#Printa tabellen med ord
print("Här kommer tabellen med ord och hur många av varje det fanns")
for ord in ordLista:
    pos = ordLista.index(ord)
    print(ord, " ", antalOrdLista[pos])