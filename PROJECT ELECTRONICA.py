# # # # # # # # games = [ "0", "1" , "2" ]

# # # # # # # # for game in games:
# # # # # # # #     print (game)


# # # # # # # # print(games[0])

# # # # # # # # max = len(games[0])-1
# # # # # # # # print (games[max])






# # # # # # # punten = [12, 15, 18, 9]

# # # # # # # print(sum(punten))
# # # # # # # print(max(punten))







# # # # # # namen = [input("Naam 1: "), input("Naam 2: "), input("Naam 3: ")]

# # # # # # for naam in namen:
# # # # # #     print(naam)




# # # # # producten = ["kaas", "hesp", "melk"]

# # # # # verwijderd = input("welk product moet verwijderd worden?: ")
# # # # # producten.remove(verwijderd)

# # # # # print(producten)




# # # # punten = [16, 22, 23, 4]


# # # # print(punten)
# # # # print(sum(punten)/len(punten))
# # # # print(max(punten))
# # # # print(min(punten))



# # # # Klassenlijst beheren
# # # # TODO: gebruik deze lijst om alle namen in op te slaan
# # # klassenlijst = []

# # # while True:
# # #     print("\n--- Klassenlijst beheren ---")
# # #     print("1. Naam toevoegen")
# # #     print("2. Naam verwijderen")
# # #     print("3. Toon lijst")
# # #     print("4. Zoek leerling")
# # #     print("5. Stoppen")

# # #     keuze = input("Maak een keuze (1-5): ")

# # #     if keuze == "1":
# # #          toe = input("welke naam toevoegen?: ")
# # #          klassenlijst.append(toe)
        
        
        
# # #         pass

# # #     elif keuze == "2":
# # #         klassenlijst = []

# # #         naam = input("welke naam verwijderen?: ")
# # #         if naam in klassenlijst:
# # #             print("Gevonden")
        
# # #         klassenlijst.remove(naam)
# # #         print("succses!!!")
        
        
        
# # #         pass

# # #     elif keuze == "3":
# # #         klassenlijst  = []
        
        
# # #         pass

# # #     elif keuze == "4":
        
# # #         naam = input("welke naam zoeken?: ")
# # #         if naam in klassenlijst:
# # #             print("Gevonden")
        
        
        
# # #         pass

# # #     elif keuze == "5":
# # #         print("Programma gestopt.")
# # #         break

# # #     else:
# # #         print("Ongeldige keuze, probeer opnieuw.")


# # # Klassenlijst beheren
# # klassenlijst = []

# # while True:
# #     print("\n--- Klassenlijst beheren ---")
# #     print("1. Naam toevoegen")
# #     print("2. Naam verwijderen")
# #     print("3. Toon lijst")
# #     print("4. Zoek leerling")
# #     print("5. Stoppen")

# #     keuze = input("Maak een keuze (1-5): ")

# #     if keuze == "1":
# #         toe = input("welke naam toevoegen?: ")
# #         klassenlijst.append(toe)

# #     elif keuze == "2":
# #         naam = input("welke naam verwijderen?: ")
# #         if naam in klassenlijst:
# #             klassenlijst.remove(naam)
# #             print("Succes verwijderd!")
        

# #     elif keuze == "3":
# #         print("Lijst:", klassenlijst)

# #     elif keuze == "4":
# #         naam = input("welke naam zoeken?: ")
# #         if naam in klassenlijst:
# #             print("Gevonden!")
# #         else:
# #             print("Niet gevonden.")

# #     elif keuze == "5":
# #         print("Programma gestopt.")
# #         break

# #     else:
# #         print("Ongeldige keuze, probeer opnieuw.")


# punten = [12, 15, 8, 20]

# grootste = punten[0]
# for punt in punten:
#     if punt > grootste:
#         kleinste = punt

# print(grootste)

lijst = [5, 2, 8, 1]

for i in range(len(lijst)):
    KI = i

    for j in range(i + 1, len(lijst)):
        if lijst[j] < lijst[KI]:
            KI = j

    lijst[i], lijst[KI] = lijst[KI], lijst[i]

print(lijst)