summa = 0
storst = 0
count = 0

tal = int(input("Tal: "))
while tal >= 0:
    summa += tal
    if tal > storst:
        storst = tal
    count += 1        
    tal = int(input("Tal: "))
else:
    print("Du avslutade med", tal)

print("Summa =", summa)
print("Störst =", storst)
if count > 0:
    print("Medel =", summa / count)
