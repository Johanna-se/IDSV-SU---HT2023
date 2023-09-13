try:
    counts = [0] * 100
    file = open("igelkott.txt","r")
    for line in file:
        line = line.strip()
        words = line.split(" ")
        for w in words:
            counts[len(w)] += 1
    file.close()
    for pos in range(len(counts)):
        if counts[pos] > 0:
            print(pos,":",counts[pos])
    
except FileNotFoundError:
    print("Hittar inte filen!")
