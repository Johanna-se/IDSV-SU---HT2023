# Lärarens lösning på uppgift 4 som hör till föreläsning 6

freqs = [0] * 26                #Speciellt för python, kommandot upprepar listan 26 gånger
text = input("Text: ")

for letter in text:
    if letter >= "A" and letter <= "Z":
        freqs[ord(letter) - ord("A")] += 1

for nr in range(len(freqs)):
    if freqs[nr] > 0:
        print(chr(nr + 65), freqs[nr])