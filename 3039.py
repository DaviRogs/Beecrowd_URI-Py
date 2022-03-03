#Numero de crianças (N)
N = int(input())

#Inicialmente, terão 0 carrinhos e bonecas
car = 0
bon = 0

#Enquanto N for maior que 0, faça:
while N != 0:
    #O usuário dirá o nome e o sexo da criança
    NS = input().split() # (Divide os dois valores, um para N e outro para S)
    No = NS[0]
    S = NS[1].upper() #Forçar a string para letra maiúscula

    #Se a pessoa for M (Masculino), faça:
    if S == 'M':
        car += 1 # (0 = 0 + 1, logo a quantidade de carros será q quantidade de carros anteriormente + 1)
    else:
        bon += 1 # (0 = 0 + 1, logo a quantidade de bonecas será q quantidade de bonecas anteriormente + 1)
    
    #Passará para a próxima criança, repetindo o processo até que N seja igual a 0
    N -= 1

print('{} carrinhos'.format(car))
print('{} bonecas'.format(bon))
