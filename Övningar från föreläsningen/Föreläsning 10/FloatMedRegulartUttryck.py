import re

pattern = r"^[-+]?[0-9]*\.?[0-9]+$"
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