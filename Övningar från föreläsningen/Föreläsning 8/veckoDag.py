dayNames = ["måndag", "tisdag", "onsdag", "torsdag", "fredag", "lördag", "söndag"]
monthNames = ["Januari", "Februari", "Mars", "April", "Maj", "Juni", "Juli", "Augusti", "September", "Oktober", "November", "December"]
maxDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #Anger hur många dagar i varje månad


weekday = input("Veckodag, 1 januari: ")

#EJ rekommenderat nedan, använd while sats då användaren kan skriva fel igen
#if weekday not in dayNames:                 #Om dagen inte finns i listan
    #print("Fel veckodag, försök igen!")
    #weekday = input("Veckodag, 1 januari: ")   

while weekday not in dayNames:                 #Om dagen inte finns i listan
    print("Fel veckodag, försök igen!")
    weekday = input("Veckodag, 1 januari: ")

for wDayNr in range(7):
    if dayNames[wDayNr] == weekday:
        break

answer = input("Är det skottår? ja/nej: ")
while answer not in ["ja", "nej"]:
    print("Fel svar, försök igen!")
    answer = input("Är det skottår? ja/nej: ")

if answer == "ja":
    maxDays[1] = 29

for monthNr in range(12):
    print(monthNames[monthNr])
    # Då det är samma loop man vill printa men med ett värde som förändras, sätt detta värde som en variabel. skapar listan med denna variabel i maxDays
    for dayNr in range(maxDays[monthNr]):
        print(dayNr + 1, "    ", dayNames[wDayNr])
        wDayNr = (wDayNr + 1) % 7
