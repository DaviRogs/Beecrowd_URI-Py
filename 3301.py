Sobrinhos = input().split()
H = int(Sobrinhos[0])
Z = int(Sobrinhos[1])
L = int(Sobrinhos[2])

if (H > Z and H < L) or (H > L and H < Z):
    print("huguinho")

elif (Z > H and Z < L) or (Z < H and Z > L):
    print("zezinho")

else:
    print("luisinho")