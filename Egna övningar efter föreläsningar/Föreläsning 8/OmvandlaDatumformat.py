# Det här är en variant på exemplet från föreläsning 4 med inläsning av datum på formen
# ÅÅÅÅMMDD och utskrift av det i en annan form.
# Skriv ett Python-program som läser in datum på den angivna formen, men denna gång som en
# sträng. Dela upp strängen i delar motsvarande dagnumret, månadsnumret och årtalet.
# Skriv sedan ut datumet på formen DD månadsnamn ÅÅÅÅ.
# Använd en lista för omvandling av månadsnumret till månadsnamn.

#Variabler
monthLista = ["Januari", "Februari", "Mars", "April", "Maj", "Juni", "Juli", "Augusti", "September", "Oktober", "November", "December"]

#Hämta input från användaren
datum = input("Datum (format ÅÅÅÅMMDD): ")

#Dela upp strängen i delar för år, månad och dag
ar = datum[0:4]                                     #[0:4] delar upp strängen från första upp till (men ej inkluderat) 4
manad = int(datum[4:6])                             #Gör om månad till ett heltal för att använda som index i monthLista
dag = datum[6:8]

#Omvandla datumnamnet
manadNamn = monthLista[manad - 1]

#Print resultat på formen DD månadsnamn ÅÅÅÅ
print(dag, manadNamn, ar)
