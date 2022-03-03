B = int(input())
G = int(input())

Bolinhas_T = G/2
B = Bolinhas_T - B

if B > 0:
    print("Faltam {} bolinha(s)".format(int(B)))

else:
    print("Amelia tem todas bolinhas!")