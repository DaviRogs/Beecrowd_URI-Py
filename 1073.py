#Inserir o máximo no número
multiplicador = int(input())
multiplicado = 2

#Enquanto o valor multiplicado for menor ou igual ao valor do multiplicador, faça:
while multiplicado <= multiplicador:
        
    Result = multiplicado ** 2

    print('{}^2 ='.format(multiplicado), Result)

    multiplicado += 2

