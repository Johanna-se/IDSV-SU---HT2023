# Skriv ett Python-program som läser in orden från textfilen svenskaOrd.txt.
# Programmet ska sedan fråga användaren vilket ord hen vill rimma på och sedan skriva ut
# alla ord från ordboken som slutar med samma tre bokstäver som det ordet användaren
# matade in. Detta ska upprepas tills användaren matar in "sluta" som ord att rimma på.
# Om filen svenskaOrd.txt inte kan öppnas (t.ex. inte finns i aktuell mapp) ska ett
# vänligt felmeddelande ges (undantaget heter då FileNotFoundError).


#Försök öppna filen
try:
    #hårdkodad vilken fil som ska öppnas
    file = open("svenskaOrd.txt", "r")

    #Läs in filen och stäng den sedan
    ordLista = file.readlines()
    file.close()

    #Loopa igenom varje element 
    for pos in range(len(ordLista)):
        ordLista[pos] = ordLista[pos].strip()               #Ta bort new line tecken

    
except FileNotFoundError:
    print("Hittade inte filen!")

