M = int(input())
A = int(input())
B = int(input())

C = M - (A + B)

if A > B:
    if A > C:
        print(A)
    else:
        print(C)
else:
    if B > C:
        print(B)
    else:
        print(C)