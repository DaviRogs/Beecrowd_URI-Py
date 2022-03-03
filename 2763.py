CPF = input()
CPF = CPF.replace('-', '.')
CPF = CPF.split('.')

for i in CPF:
    print(i)