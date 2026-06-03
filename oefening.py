namen = ["Emma", "Lucas", "Noah", "Liam"]

naam = input("Welke naam wil je zoeken?: ")
        
if naam in namen:
    i = namen.index(naam)
    print("gevonden" , i)
else:
    print("niet gevonden")
    
stap = int(input("1. naam toevoegen, 2. stoppen: , 3. naam verwijderen "))

if stap == 1:         
    naam = input("welke naam wil je toevoegen?: ")
    namen.append(naam)
    print(namen)
    
    
elif stap == 2:
    print("Programma gestopt.")
    
elif stap ==3:
    print(namen)
    naam = input("welke naam wil je verwijderen?: ")
    if naam in namen:
        namen.remove(naam)
        print(namen)
    else:
        print("Deze naam staat niet in de lijst.")
    