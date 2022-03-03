n = int(input()) # Quantidade de movimentos
copoin = input()
A = False # Copo A
B = False # Copo B
C = False # Copo C

if copoin == "A":
    A = True

elif copoin == "B":
    B = True

elif copoin == "C":
    C = True


for i in range(n):
    mov = int(input())

    if mov == 1:
        if A == True:
            A = False
            B = True
        elif B == True:
            B = False
            A = True
    
    if mov == 2:
        if B == True:
            B = False
            C = True
        elif C == True:
            C = False
            B = True

    if mov == 3:
        if A == True:
            A = False
            C = True
        elif C == True:
            C = False
            A = True

if A == True:
    print("A")

elif B == True:
    print("B")

elif C == True:
    print("C")