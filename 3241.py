N = int(input())

for i in range(N):
    operacao = input().split("+")

    if operacao[0] == "P=NP":
        print("skipped")

    else:
        operacao = int(operacao[0]) + int(operacao[1])

        print(operacao)