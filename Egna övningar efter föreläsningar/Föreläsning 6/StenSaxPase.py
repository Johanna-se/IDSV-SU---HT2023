# Övnings beskrivning:
# Skriv ett Python-program som spelar sten-sax-påse med användaren.
# Programmet ska läsa in användarens val och sedan slumpa fram sitt val av de tre orden.
# Sedan ska programmets val och användarens val jämföras enligt spelets regler (kolla dem på
# webben om du inte känner till dem) och den som vinner får en poäng.
# Detta ska fortsätta tills användaren matar in ”sluta” som sitt val.
# Då ska ställningen mellan programmet och användaren skrivas ut.
# I modulen random som introducerades i uppgift 2 finns en funktion choice() som kan ta
# en lista som argument och returnerar ett slumpmässigt element från den listan. Den kan t.ex.
# anropas så här:
# val = random.choice(["sten","sax","påse"])
# varpå variabeln val kommer att innehålla ett av dessa ord, slumpmässigt valt.


import random

#Uppstart
AnvandarVal = "Börja"
PoangDator = 0
PoangAnvandare = 0

#Hälsningsfras
print("Hej och välkommen till Sten-Sax-Påse. Skriv vilket av de tre alternativen du väljer och så spelar vi. För att avsluta skriv: Sluta")

while AnvandarVal != "Sluta":
    val = random.choice(["sten","sax","påse"])
    AnvandarVal = input("Vad vill du spela?: ")

    if AnvandarVal != "Sluta":
        print("Datorn valde:", val)

    if val == AnvandarVal:
        print("Båda valde", val, "och det blev oavgjort")
    elif val == "sten" and AnvandarVal == "sax":
        print("Nu vann datorn, poäng till den.")
        PoangDator += 1
    elif val == "sax" and AnvandarVal == "sten":
        print("Nu vann du, poäng till dig.")
        PoangAnvandare += 1
    elif val == "sax" and AnvandarVal == "påse":
        print("Nu vann datorn, poäng till den.")
        PoangDator += 1
    elif val == "påse" and AnvandarVal == "sax":
        print("Nu vann du, poäng till dig.")
        PoangAnvandare += 1
    elif val == "påse" and AnvandarVal == "sten":
        print("Nu vann datorn, poäng till den.")
        PoangDator += 1
    elif val == "sten" and AnvandarVal == "påse":
        print("Nu vann du, poäng till dig.")
        PoangAnvandare += 1
    elif AnvandarVal != "Sluta":
        print("Nu blev det fel. prova igen")
    
print("Poängen blev: Dator", PoangDator, "och din poäng", PoangAnvandare)
