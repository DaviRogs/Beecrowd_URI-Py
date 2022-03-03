teste = 1
while True: # Início de repetição até q M seja 0
    m = int(input()) # Recebe quantidade de operadores, mas só serve pra interromper o programa.
    
    # Interrupção da repetição caso indique 0 como quantidade de operadores
    if m == 0:
        break

    calc = input()
    operadores = []
    
    # Início para separar os operadores
    for i in range(len(calc)):
        if not calc[i].isnumeric():
            operadores.append(calc[i])

    # Reorganização da lista calc, para deixar só os operandos:
    calc = calc.replace("-", "+").split("+")
    for i in range(len(calc)):
        calc[i] = int(calc[i])

    conta = calc[0]

    # Início das contas:
    for i in range(len(operadores)):
        if operadores[i] == "+": # Condiçao para caso "+"
            conta += calc[i + 1]
        else: # Condição para caso "-"
            conta -= calc[i + 1]

    print("Teste {}".format(teste))
    print(conta)
    print()
    teste += 1
    

