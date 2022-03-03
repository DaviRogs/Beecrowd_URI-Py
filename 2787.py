L = int(input())
C = int(input())

if L > C:
    Resultado = L - C
else:
    Resultado = C - L
    
if (Resultado%2) == 0:
    print('1')
else:
    print('0')