# Quantas rodadas serão realizadas (N)
N = int(input())

#Enquanto N for maior que 0, faça:
while N != 0: # (Ex: 2 > 0)
    #Inicialmente e/ou ao final e cada rodada, as pontuações de João e Maria estarão zeradas
    MPontuacao = 0
    JPontuacao = 0
    # V de "Vez(es)"
    V = 0
    #Entrada de dados da jogada de Jõao

    while V < 3: #Enquanto a vez de Jõao for menor que 3, faça:
        JXD = input().split()# (Divide os dois valores, um para JX e outro para JD)
        JX = int(JXD[0]) # (Ex: 3)
        JD = int(JXD[1]) # (Ex: 4)

        JPontuacao = JPontuacao + (JX * JD) # (0 = 0 + (3 * 4)), logo JPontuacao = 12
        V += 1 #Vai para a próxima vez de João, repetindo o processo do while até V ser maior que 3

    #Reseta a vez para Maria Jogar
    V = 0

    while V < 3: #Enquanto a vez de Maria for menor que 3, faça:
        MXD = input().split() # (Divide os dois valores, um para MX e outro para MD)
        MX = int(MXD[0]) # (Ex: 2)
        MD = int(MXD[1]) # (Ex: 1)

        MPontuacao = MPontuacao + (MX * MD) # (0 = 0 + (2 * 1)), logo MPontuacao = 2
        V += 1 #Vai para a próxima vez de Maria, repetindo o processo do while até V ser maior que 3
    
    #Se a pontuação de João ser maior que a da Maria, faça:
    if JPontuacao > MPontuacao: # (Ex: 12 > 2)
        print('JOAO') #Vitorioso

    #Caso contrário, faça:
    else:
        print('MARIA') #Vitoriosa

    #O processo anterior se fecha e vai para o próximo, até que N seja igual a 0
    N -= 1
