daynames = ["måndag","tisdag","onsdag","torsdag","fredag","lördag","söndag"]
monthnames = ["januari","februari","mars","april","maj","juni","juli",
              "augusti", "septemeber", "oktober","november","december"]
maxdays = [31,28,31,30,31,30,31,31,30,31,30,31]
weekday = input("Veckodag den 1a januari: ")
while weekday not in daynames:
    print("Fel veckodag, försök igen!")
    weekday = input("Veckodag den 1a januari: ")

for wdaynr in range(7):
    if daynames[wdaynr] == weekday:
        break

answer = input("Är det skottår? ja/nej: ")
while answer not in ["ja", "nej"]:
    print("Fel svar, försök igen!")
    answer = input("Är det skottår? ja/nej: ")

if answer == "ja":
    maxdays[1] = 29

for monthnr in range(12):
    print(monthnames[monthnr])
    for daynr in range(maxdays[monthnr]):
            print(daynr + 1, " "*5, daynames[wdaynr])
            wdaynr = (wdaynr + 1) % 7
