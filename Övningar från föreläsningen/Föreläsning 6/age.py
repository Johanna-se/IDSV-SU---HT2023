summa = 0
count = 0
stringinput = input("Ålder: ")
while stringinput != "":
    age = int(stringinput)
    if age >= 0 and (age < 16 or age > 65):
        print("Fel ålder!")
        stringinput = input("Ålder: ")
        continue
    if age < 0:
        break

    summa += age
    count += 1
    stringinput = input("Ålder: ")

if count > 0:
    print("Medelåldern =", summa / count)
    
