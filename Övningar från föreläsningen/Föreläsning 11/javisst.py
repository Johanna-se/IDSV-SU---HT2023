def pause(message, rows):
    for rad in range(rows):
        print("*" * 50)
    input(message)
    

file = open("javisst.txt")
poser = file.readlines()
file.close()

for pos in range(0, 8):
    print(poser[pos].strip())
pause("Tryck på RET", 3)

for pos in range(8, 16):
    print(poser[pos].strip())
pause("Andra raden?", 2)

for pos in range(16, 24):
    print(poser[pos].strip())
pause("Tryck på RET för att avsluta!", 2)
