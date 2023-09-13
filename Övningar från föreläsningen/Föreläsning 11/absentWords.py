try:
    file = open("svenskaOrd.txt", "r")
    words = file.readlines()
    file.close()
    for pos in range(len(words)):
        words[pos] = words[pos].strip()

    absent = set()
    filename = input("File: ")
    file = open(filename, "r")
    for line in file:
        line = line.lower()
        wordsinline = line.split()
        for w in wordsinline:
            if w not in words:
                absent.add(w)

    file.close()

    utlist = list(absent)
    utlist.sort()
    print("Följande ord saknas i svenskaOrd.txt:")
    for w in utlist:
        print(w)
        
except FileNotFoundError:
    print("Hittar inte filen", filename)
