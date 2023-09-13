while True:
    answer = input("Ålder:")
    if not answer.isdigit():
        print("Fel inmatning!")
        continue
    age = int(answer)
    if age < 16 or age > 65:
        print("Fel ålder")
    else:
        break
print("Du matade in åldern", age)