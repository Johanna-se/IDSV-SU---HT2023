# Övningsbeskrivning:
# Skriv ett Python-program som läser från användaren en textrad. Därefter ska programmet
# räkna hur många gånger varje bokstav i alfabetet (det engelska) förekommer i denna text.
# För detta bör man använda en lista, med ett heltal (som räknare) i listan för varje bokstav i
# alfabetet. Men listor indexeras med heltalsindex, inte med bokstäver. Då kan man få fram ett
# heltal för varje bokstav genom funktionen ord(tecken) (för ordinal), som tar ett tecken
# som argument och returnerar teckenkoden som ett heltal.
# Efter att alla tecken har räknats ska en tabell skrivas ut, med varje bokstav som förekom i
# texten och hur många gånger den förekom. De bokstäver som inte förekom i texten ska dock
# inte skrivas ut.

text = input("Skriv ett ord eller mening (använd inte å, ä, ö): ")
teckenlista = []

startPos = 0
slutPos = ord("~")

#Skapa listan
while startPos < slutPos:
    teckenlista += [0]
    startPos += 1

#Räkna tecknena i strängen
for tecken in text:
    pos = ord(tecken)                   #Då kan man få fram ett heltal för varje bokstav genom funktionen ord(tecken) (för ordinal), som tar ett tecken som argument och returnerar teckenkoden som ett heltal.
    teckenlista[pos] += 1

#Printa listan OBS endast de som inte är 0. 
pos = 0
for nummer in teckenlista:
    if nummer > 0:
        print(chr(pos), "=", nummer) 
    pos += 1
