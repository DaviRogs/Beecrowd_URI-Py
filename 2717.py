N = int(input())

Presentes = input().split()
A = int(Presentes[0])
B = int(Presentes[1])

Tempo = A + B

if Tempo > N:
    print('Deixa para amanha!')

else:
    print('Farei hoje!')