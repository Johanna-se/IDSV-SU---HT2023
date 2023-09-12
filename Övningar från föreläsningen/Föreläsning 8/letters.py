freqs = [0] * 26
text = input("Text: ")
for letter in text:
    if letter >= "A" and letter <= "Z":
        freqs[ord(letter) - 65] += 1

for nr in range(len(freqs)):
    if freqs[nr] > 0:
        print(chr(nr + 65), freqs[nr])
