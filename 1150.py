X = int(input())
Z = int(input())
Cont = 0

if Z <= X:
    while Z <= X:
        Z = int(input())

while X <= Z:
    X = X + (X + 1)
    Cont = Cont + 1

print(int(Cont + 2))