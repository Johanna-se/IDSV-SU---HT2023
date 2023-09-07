bokstav = input("Ange en bokstav och jag ska säga om det är en kosonant eller en vokal: ")

# Skapa lista med vokaler
vokaler = ["a", "e", "i", "o", "u", "ä", "å", "ö", "A", "E", "I", "O", "U", "Å", "Ä", "Ö"]  


if bokstav in vokaler:
    print(bokstav, "är en vokal.")
else:
    print(bokstav, "är en konsonant.")