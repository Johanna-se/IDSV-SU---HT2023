talen = []
tal = int(input("Tal: "))
while tal >= 0:
    talen += [tal]
    tal = int(input("Tal: "))

kom = input("Kommando: ")
while kom != "sluta":
    match kom:
        case "skriv":
            for num in talen:
                print(num, end=" ")
            print()
        case "summa":
            summa = 0
            for num in talen:
                summa += num
            print("Summa =", summa)
        case "addera":
            pos = int(input("Position: "))
            if pos < 0 or pos >= len(talen):
                print("Fel position!")
            else:
                num = int(input("Att addera: "))
                talen[pos] += num
        case "sluta":
            pass
        case _:
            print("Fel kommando!")            
    kom = input("Kommando: ")
