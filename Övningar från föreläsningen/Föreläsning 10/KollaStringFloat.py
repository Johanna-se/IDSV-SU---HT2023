while True:
    answer = input("Vikt:")
    if not answer.replace(".","",1).isdigit():      #Byter ut . mot inget. 1an anger att det endast är första punkten som ska bytas ut. Om fler punkter så är det ändå angivet på fel format
        print("Fel inmatning!")
        continue
    vikt = float(answer)
    if vikt < 20.0 or vikt > 600.0:
        print("Fel vikt, ska vara mellan 20 och 600!")
    else:
        break
print("Du matade in vikten", vikt)