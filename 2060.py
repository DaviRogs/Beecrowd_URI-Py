#Entrada da quantidade de números
quant = int(input())
quant -= 1

#Entrada dos números
num = input().split()

#Inicialmente, a quantidades dos múltiplos estarão zeradas
Qmult2 = 0
Qmult3 = 0
Qmult4 = 0
Qmult5 = 0

#Enquanto a Quantidade de números ser diferente de 0, faça:
while quant >= 0:

    #Se o número[em relação ao número da quantidade, assim pegando na lista de num] for igual a 0, faça:
    if int(num[quant]) % 2 == 0: # (Ex: num[0] é o 10 e dividindo pr 2, terá como resto 0)
        Qmult2 += 1 # (logo, a essa validação será acresentado na quantidade de múltiplo de 2)
    
    #Caso o número[em relação ao número da quantidade, assim pegando na lista de num] for igual a 0, faça:
    if int(num[quant]) % 3 == 0:
        Qmult3 += 1

    #Caso o número[em relação ao número da quantidade, assim pegando na lista de num] for igual a 0, faça:
    if int(num[quant]) % 4 == 0:
        Qmult4 += 1

    #Caso o número[em relação ao número da quantidade, assim pegando na lista de num] for igual a 0, faça:
    if int(num[quant]) % 5 == 0:
        Qmult5 += 1

    #Obs: Todos os valores devem ser avaliados em cada múltiplo, por isso descarta o elif ou else!
    
    quant -= 1

print('{} Multiplo(s) de 2'.format(Qmult2))
print('{} Multiplo(s) de 3'.format(Qmult3))
print('{} Multiplo(s) de 4'.format(Qmult4))
print('{} Multiplo(s) de 5'.format(Qmult5))
