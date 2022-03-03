Copos = input().split()
C1 = int(Copos[0])
C2 = int(Copos[1])
C3 = int(Copos[2])
C4 = int(Copos[3])

if (C1 == 1) and C2 == 0 and C3 == 0 and C4 == 0:
    print('1') 

if C1 == 0 and (C2 == 1) and C3 == 0 and C4 == 0:
    print('2')

if C1 == 0 and C2 == 0 and (C3 == 1) and C4 == 0:
    print('3')

if C1 == 0 and C2 == 0 and C3 == 0 and (C4 == 1):
    print('4')