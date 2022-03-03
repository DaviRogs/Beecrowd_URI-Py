n = int(input())

for i in range(n):
    K = input().split() 
    r = int(K[0]) 

    b = 1
    t = 0
    while b <= r: 
        li = int(K[b]) 

        t += li 
        b += 1

    t -= (r-1) 
    print(t)