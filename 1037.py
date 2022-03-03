Intervalo = float(input())

if ((Intervalo >= 0) and (Intervalo <= 25)):
    print("Intervalo [0,25]")

if ((Intervalo > 25) and (Intervalo <= 50)):
    print("Intervalo (25,50]")

if ((Intervalo > 50) and (Intervalo <= 75)):
    print("Intervalo (50,75]")

if ((Intervalo > 75) and (Intervalo <= 100)):
    print("Intervalo (75,100]")

if ((Intervalo < 0) or (Intervalo > 100)):
    print("Fora de intervalo")