# 3.4 
gastenLijst = []
aantal=int(input("Hoeveel mensen wil je uitnodigen.\n"))
while aantal > 0:
    gastenLijst.append(input( "Geef de naam\n"))
    aantal = aantal - 1

z = 66


for name in gastenLijst:
    print(f"Hallo {name}\n graag nodig ik jou uit voor mijn etentje ")