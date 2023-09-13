# Skriv ett Python-program som fungerar som en liten svensk-engelsk ordbok.
# Skapa i programmet två listor med strängar: en med svenska ord och den andra med
# motsvarande engelska ord. Var noga med att de svenska orden och motsvarande engelska ord
# ligger på samma position i var sin lista. Programmet ska sedan i en loop läsa in ett svenskt ord
# och skriva ut motsvarande engelska ord. Om det inlästa svenska ordet inte finns i svenska
# listan ska ett felmeddelande skrivas ut. Programmet ska avslutas när användaren matat in
# ordet ”sluta” som svenskt ord. Det ska inte spela någon roll om användaren matar in de
# svenska orden med versaler, gemena eller en blandning av dessa.
# Lägg inte ner mycket tid på att hitta på de svenska och engelska orden, de behöver inte vara
# många – strukturen i programmet blir likadant ändå.
# Obs! att det finns bättre lösningar än två listor för att lösa detta problem, men vi har inte tagit
# upp dem än, och övningen är en bra övning på listor.

#Skapa ordlistor
SvLista = ["hej", "blå", "anka", "vem"]
EngLista = ["hello", "blue", "duck", "who"]

#Be om avändarens input
anvInput = input("Skriv ett svenskt ord (skriv sluta för att avsluta):")
anvInputFormat = anvInput.lower()                                           #Ser till att alla bokstäver är versaler

#Loopa tills användaren skriver sluta
while anvInputFormat != "sluta":
    #Hitta om det svenska ordet finns i listan
    if anvInputFormat in SvLista:
        #Titta index för det svenska ordet
        pos = SvLista.index(anvInputFormat)
        #Printa det engelska motsvarigheten
        print("Det engelska ordet för ", anvInput, "är", EngLista[pos])
    else:
        print("Tyvärr hittades inte det ordet i listan. försök igen.")

    #Hämta input från användaren igen
    anvInput = input("Skriv ett svenskt ord (skriv sluta för att avsluta):")
    anvInputFormat = anvInput.lower() 

print("Välkommen åter.")