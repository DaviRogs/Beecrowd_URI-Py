NPal = int(input())
Cont = 0


while Cont != NPal:
    Palavra = input()
    
    if(len(Palavra) > 3):
        acertos = 0
        if Palavra[0:1]=='t':
            acertos += 1
        
        if Palavra[1:2]=='h':
            acertos += 1

        if Palavra[2:3]=='r':
            acertos += 1
        
        if Palavra[3:4]=='e':
            acertos += 1
        
        if Palavra[4:5]=='e':
            acertos += 1

        if acertos >= 4:
            print('3')
            acertos = 0

    else:
        acertos = 0
        if Palavra[0:1]=='o':
            acertos += 1
        
        if Palavra[1:2]=='n':
            acertos += 1

        if Palavra[2:3]=='e':
            acertos += 1
        
        if acertos >= 2:
            print('1')
    
        else:
            print('2')
    
    Cont += 1