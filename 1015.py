PrimeiraLinha = input().split()
x1 = float(PrimeiraLinha[0])
y1 = float(PrimeiraLinha[1])

SegundaLinha = input().split()
x2 = float(SegundaLinha[0])
y2 = float(SegundaLinha[1])

dist = ((x2 - x1)**(2) + (y2 - y1)**(2)) ** (1/2)

print(round(dist, 4))