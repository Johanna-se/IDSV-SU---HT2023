# Skriv ett Python-program som läser in orden från textfilen svenskaOrd.txt.
# Programmet ska sedan fråga användaren vilket ord hen vill rimma på och sedan skriva ut
# alla ord från ordboken som slutar med samma tre bokstäver som det ordet användaren
# matade in. Detta ska upprepas tills användaren matar in "sluta" som ord att rimma på.
# Om filen svenskaOrd.txt inte kan öppnas (t.ex. inte finns i aktuell mapp) ska ett
# vänligt felmeddelande ges (undantaget heter då FileNotFoundError).

#Skapa en lista att förvara orden i 
ordLista = []

#Försök öppna filen
try:
    file = open("svenskaOrd.txt", "r")
    
    #Loopa igenom varje rad och lägg till i ordlistan
    for line in file:
        line = line.strip()             #Ta bort så att det inte blir en ny rad
        ordLista.append(line)
except FileNotFoundError:
    print("Hittade inte filen!")

#test
for ord in range(10):
    print(ordLista[ord])