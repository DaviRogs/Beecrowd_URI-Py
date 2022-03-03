EFC = input().split() # Número de garrafas vazias, garrafas vazias encontradas, minimo de garrafas para troca

EF = int(EFC[0]) + int(EFC[1]) # É somada todas as garrafas vazias em mãos
C = int(EFC[2]) # Armazena-se a informação do mínimo de garrafas necessárias

full = 0 # Declaração para guarrafas cheias

# Iniciação para se calcular quantas cheias terá em mãos
while EF >= C:
    EF -= C
    full += 1

drink = 0 # Declaração para garrafas ingeridas

# Baseando-se nas garrafas cheias, estas serão subtraídas pelo número de garrafas mínimas até não dar mais
while full > 0:
    full -= C

    if full < 0: # Caso não tenha o mínimo de garrafas para trocar, a repetição é interrompida.
        full += C 
        break

    full += 1 # Para cada garrafa trocada, será adicionada mais 1 guarrafa cheia
    drink += C # Será contabilizado o consumo do cachaceiro a cada repetição

# Caso tenha sobrado guarrafa na primeira iniciação, este if irá verificar se juntando 
# com as garrafas vazias apos toma-las derá para trocar por mais 1 cheia
if (EF + full) >= C:
    drink += 1

print(drink + full)