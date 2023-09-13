# Skriv ett Python-program som läser från användaren en lång textrad bestående av flera ord
# avdelade med mellanslag. Med ord här menas bara följder av icke-blanka tecken avslutade av
# mellanslag eller slutet på strängen. Programmet ska skriva ut hur många ord som finns i
# texten och vilket som är det längsta ordet.

#Be användaren om en mening
anvandresInput = input("Skriv en mening: ")

#Splitta meningen till en lista med ett ord på varje index
ordLista = anvandresInput.split()
langstaOrdet = 0
langstaOrdetPos = 0

#printa listan
for ord in ordLista:
    print(ord)

    #hitta det längsta ordet
    if len(ord) > langstaOrdet:
        langstaOrdet = len(ord)
        langstaOrdetPos = ordLista.index(ord)

print("Antal ord i meningen:", len(ordLista))
print("Längsta ordet hade", langstaOrdet, " bokstäver och var", ordLista[langstaOrdetPos])