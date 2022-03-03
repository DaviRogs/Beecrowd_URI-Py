Qelfos = int(input()) #Quantidade de elfos
cont = 0 #Contador
TBPresente = 0 #Total Presentes de Bonecas
TAPresente = 0 #Total Presentes de Arquitetos
TMPresente = 0 #Total Presentes de Musicos
TDPresente = 0 #Total Presentes de Desenhistas
BSobra = 0 
ASobra = 0
MSobra = 0
DSobra = 0

#Enquanto o contador for diferente da Quantidade de elfos, faça:
while cont != Qelfos:
    NSH = input().split() #NSH - Nome Setor Horas
    Nome = NSH[0]
    Setor = NSH[1].lower()
    Horas = int(NSH[2])
    BPresente = Horas
    APresente = Horas
    MPresente = Horas
    DPresente = Horas

    #Se o Setor for Bonecos, faça:
    if Setor == 'bonecos':
        while BPresente >= 0:
            BPresente -= 8 #Tirando 8 horas do trabalho dele, será produzido 1 boneco
            #Se o a subtração do horário ainda for maior ou igual a 0, será acrescentado no total de bonecos
            if BPresente >= 0:
                TBPresente += 1
        
        #Caso o tempo tenha ultrapassado, significa que teve uma sobra de tempo, vamos armazená-la usando:
        if BPresente < 0:
            BSobra = BSobra + (BPresente + 8)
        
    elif Setor == 'arquitetos':
        while APresente >= 0:
            APresente -= 4
            if APresente >= 0:
                TAPresente += 1
        
        if APresente < 0:
            ASobra = ASobra + (APresente + 4)

    elif Setor == 'musicos':
        while MPresente >= 0:
            MPresente -= 6 
            if MPresente >= 0:
                TMPresente += 1
        
        if MPresente < 0:
            MSobra = MSobra + (MPresente + 6)
    
    elif Setor == 'desenhistas':
        while DPresente >= 0:
            DPresente -= 12
            if DPresente >= 0:
                TDPresente += 1
        
        if DPresente < 0:
            DSobra = DSobra + (DPresente + 12)


    cont += 1

#Verificação da soma de todos os horários dos trabalhadores de um mesmo grupo:
if BSobra >= 8:
    while BSobra >= 0:
        BSobra -= 8 #Tirando 8 horas do trabalho dele, será produzido 1 boneco
        #Se o a subtração do horário ainda for maior ou igual a 0, será acrescentado no total de bonecos
        if BSobra >= 0:
            TBPresente += 1

if ASobra >= 4:
    while ASobra >= 0:
        ASobra -= 4
        if ASobra >= 0:
            TAPresente += 1
    
if MSobra >= 6:
    while MSobra >= 0:
        MSobra -= 6
        if MSobra >= 0:
            TMPresente += 1
    
if DSobra >= 12:
    while DSobra >= 0:
        DSobra -= 12
        if DSobra >= 0:
            TDPresente += 1

print(TBPresente + TAPresente + TMPresente + TDPresente)