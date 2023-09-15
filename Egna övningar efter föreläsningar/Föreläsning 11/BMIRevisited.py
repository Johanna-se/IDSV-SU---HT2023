# Tillsammans med den här texten en lösning på övningsuppgiften med BMI-beräkning.
# Den börjar med två nästan likadana kodsnuttar för inläsning av vikt resp. längd med
# rimlighetskontroll.
# Skriv om programmet med en funktion som gör inläsningen istället, så att man slipper
# upprepning av kod .
# Funktionen ska alltså läsa in ett float-tal och göra en rimlighetskontroll av talet.
# Funktionen ska returnera det inlästa talet.
# De värden som skiljer de två kodsnuttarna åt får bli parametrar till funktionen

# Från föreläsning 4a:
# Utöka BMI-uppgiften från övningar efter F2 med att även skriva ut viktklass enligt följande
# tabell:
# Mindre än 18.5    underviktig
# 18.5 - 24.9       Normalviktig
# 25.0 - 29.9       Överviktig
# Över 30           fetma

#Från föreläsning 2:
# Skriv ett Python-program som frågar användaren om hens vikt i kg och hens längd i meter och
# som beräknar och skriver ut hens BMI (Body Mass Index).
# BMI räknas ut som vikten dividerad med längden i kvadrat:
# bmi = vikt / langd2
# Exempel på programdialogen (användarens inmatning i svart):
# Vikt: 83.2
# Längd: 1.76
# BMI = 26.859504132231407

#Funktion
def InputMedMinMaxKoll(meddelande, min, max):
    while True:
        indata = float(input(meddelande))

        if indata < min:
            print("Det var för lite, prova igen.")
        elif indata > max:
            print("Det var för mycket, prova igen.")
        else:
            break
    return indata

#Konstaner för min / max för längd och vikt
minLangd = 1
maxLangd = 2.5
minVikt = 40
maxVikt = 600

#Be om läng och vikt från användaren
Langd = InputMedMinMaxKoll("Vad är din längd (i meter)? ", minLangd, maxLangd)
Vikt = InputMedMinMaxKoll("Vad är din vikt? ", minVikt, maxVikt)

#Beräkna BMI
BMI = Vikt/Langd**2

#Kontrollera BMI mot tabell
if BMI < 18.5:
    print ("Ditt BMI är ", BMI, ". Du är underviktig")
elif 18.5 <= BMI < 25:
    print ("Ditt BMI är ", BMI, ". Du har normalvikt")
elif 25 <= BMI < 29.9:
    print ("Ditt BMI är ", BMI, ". Du är överviktig")
else:
    print ("Ditt BMI är ", BMI, ". Du har fetma")