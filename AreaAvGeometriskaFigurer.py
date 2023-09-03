figur = input("Vilken geometriska figur vill du beräkna arean på? ")

match figur:
    case "cirkel":
        radien = int(input("Vad är radien (ange i heltal): "))
        area = 3.14 * radien                                        #Har förmiskat pi till 3.14
        print("Radien är ", area)
    case "kvadrat":
        basen = int(input("Vad är basen (ange i heltal): "))
        hojden = int(input("Vad är höjden (ange i heltal): "))
        area = basen * hojden
        print("Radien är ", area)
    case "triangel":
        basen = int(input("Vad är basen (ange i heltal): "))
        hojden = int(input("Vad är höjden (ange i heltal): "))
        area = basen * hojden / 2.
        print("Radien är ", area)
    case _:
        print("Okänd form.")