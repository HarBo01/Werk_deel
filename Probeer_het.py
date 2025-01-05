# 3.4 
gastenLijst = []
aantal=int(input("Hoeveel mensen wil je uitnodigen.\n"))
while aantal > 0:
    gastenLijst.append(input( "Geef de naam\n"))
    aantal = aantal - 1

print("Ik ga hier morgen aan verder werken")



for name in gastenLijst:
    print(f"Hallo {name}\n graag nodig ik jou uit voor mijn etentje ")

# 3.5 Gastenlijst veranderen
