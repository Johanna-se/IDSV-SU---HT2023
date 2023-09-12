scale = input("Skala: ")

if scale == "Celsius":
    cels = float(input("Grader Celsius: "))
    fahr = cels * 1.8 + 32
    print("Grader Fahrenheit: ", fahr)
else:
    fahr = float(input("Grader Fahrenheit: "))
    cels = (fahr - 32) / 1.8
    print("Grader Celsius: ", cels)
print("Välkommen åter!")
