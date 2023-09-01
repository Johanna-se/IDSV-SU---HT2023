fot = int(input("Hur många fot? "))
tum = int(input("Hur många tum? "))

fotTill = int(input("Hur många fot att addera? "))
tumTill = int(input("Hur många tum att addera? "))

totalTum = fot * 12 + fotTill*12 + tum + tumTill
totalFot = totalTum//12
totalTum = totalTum % 12

print("Det totala värdet blir ", totalFot, "fot och ", totalTum, "tum")