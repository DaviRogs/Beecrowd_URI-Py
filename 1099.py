N = int(input())

while N > 0:
    #Recebe os 2 valoes do input e separa-os, um para X e outro para Y.
    XY = input().split()
    X = int(XY[0])
    Y = int(XY[1])
    Soma = 0

    #Se o valor de X for maior que Y, faça:
    if X > Y: # (Ex: 3 > 1)
        F = Y + 1 # (F = 1 + 1, logo Y é 2)
        #Enquanto F é diferente de X, faça:
        while F != X: # (F (2) Diferente de X (3))
            #Se o resto da divisão de F por 2 for diferente de 0, faça:
            if (F % 2) != 0: # 2 % 2 = 0, logo ele irá pular a condição 
                Soma = Soma + F
            # F (2) = 2 + 1, ou seja, F receberá a nova variável 3 e voltará no while para ver as condições novas
            F += 1 

    #Se o valor de X for menor que Y, faça:
    if X < Y: # (Ex: 1 < 3)
        F = X + 1 # (F = 1 + 1, logo Y é 2)
        #Enquanto F é diferente de Y, faça:
        while F != Y: # (F (2) é diferente de Y (3))
            #Se o resto da divisão de F por 2 for diferente de 0, faça:
            if (F % 2) != 0: # (2 % 2 = 0, logo ele irá pular a condição)
                Soma = Soma + F
            # F (2) = 2 + 1, ou seja, F receberá a nova variável 3 e voltará no while para ver as condições novas
            F += 1

    #Se o valor de X for igual de Y, faça:
    if X == Y: # (Ex: 0 == 0)
        Soma = 0
    
    #Apresentando o resultado.
    print(Soma)
    #Permite que o usuário faça outra entrada perdendo 1 pelo fato de ter feito um anteriormente.
    N -= 1
