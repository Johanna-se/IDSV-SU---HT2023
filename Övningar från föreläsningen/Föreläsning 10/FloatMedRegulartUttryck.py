import re

pattern = r"^[-+]?[0-9]*\.?[0-9]+$" # ^ = Här börjar strängen, [-+]? att det kan finnas antinget ett + eller -, ? anger att det inte är ett måste att det finns. [0-9]* att det kan finnas siffror efter det, * anger att det kan vara 0 eller flera. \.? betyder att det kommer kanske en . dock i och med ? å måste inte detta ske. [0-9]+ anger att det kommer minst en siffra. + har alltså samma funktion som * dock med minst 1 siffra istället för 0 eller fler. $ avslutar
while True:
    answer = input("Vikt:")
    if not re.match(pattern, answer):
        print("Fel inmatning!")
        continue
    vikt = float(answer)
    if vikt < 20.0 or vikt > 600.0:
        print("Fel vikt, ska vara mellan 20 och 600!")
    else:
        break
print("Du matade in vikten", vikt)