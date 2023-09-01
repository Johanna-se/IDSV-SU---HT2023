FyraSiffror = int(input("Skriv fyra siffror: "))

ForstaSiffran = FyraSiffror % 10
AndraSiffran = FyraSiffror // 10 % 10
TredjeSiffran = FyraSiffror // 100 % 10
FjardeSiffran = FyraSiffror // 1000 

print("Här kommer sifforna i ordning: ", ForstaSiffran, AndraSiffran, TredjeSiffran, FjardeSiffran)
print("Tillsammans blir de: ", ForstaSiffran + AndraSiffran + TredjeSiffran + FjardeSiffran)