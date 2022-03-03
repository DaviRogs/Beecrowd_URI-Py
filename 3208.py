while True: #Enquanto f for verdadeiro, faça:
    f = True
    p = 0
    k, l = map(int, input().split())
    if k == 0 and l == 0: #Se k for 0 e l for 0, faça:
        break #Quebra o looping
    for i in range(2, l): #i será o contador de 2 até l
        if k % i == 0: #Se k tiver resto da divisão por i, faça:
                p = i 
                f = False
                break
    if f:
        print("GOOD")
    else:
        print("BAD", p)