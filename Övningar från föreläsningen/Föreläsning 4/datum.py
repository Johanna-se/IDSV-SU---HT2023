datum = int(input("Datum: "))
day = datum % 100
month = datum // 100 % 100
year = datum // 10000
print("Datum var ", day, "-", month, "-", year, sep=""
