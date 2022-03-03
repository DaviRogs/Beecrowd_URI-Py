Creditos = input().split()
C1 = (int(Creditos[0]))
C2 = (int(Creditos[1]))
C3 = (int(Creditos[2]))

c1mc2 = C1 - C2
c1mc3 = C1 - C3
c2mc3 = C2 - C3
c1sc2mc3 = C1 + C2 - C3
c1sc3mc2 = C1 + C3 - C2
c2sc3mc1 = C2 + C3 - C1

if (c1mc2 == 0) or (c1mc3 == 0) or (c2mc3 == 0) or (c1sc2mc3 == 0) or (c1sc3mc2 == 0) or (c2sc3mc1 == 0):
    print('S')

else:
    print('N')