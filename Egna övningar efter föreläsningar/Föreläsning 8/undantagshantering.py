while True:
    try:
        age = int(input("Ålder: "))
        if age < 16 or age > 65:
            print("Fel ålder!")
        else:
            break
    except ValueError:
        print("Fel inmatning!")
print("Du matade in åldern", age)