heightString = input("Höjd: ")
height = float(heightString)
time = (height * 2 /9.81) ** 0.5
print("Tiden =", time, "sekunder")
