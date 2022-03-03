import datetime
from math import floor


n = int(input())

sat = 29.6
jup = 11.9

anosEmJup = jup*n

dataInicial = datetime.date(2020,12,21)

time = datetime.timedelta(anosEmJup*365.25)

print("Dias terrestres para Jupiter = {}" .format(floor(anosEmJup*365.25)))

print("Data terrestre para Jupiter: {}" .format(dataInicial + time))

anosEmSat = sat*n

time = datetime.timedelta(anosEmSat*365.25)

print("Dias terrestres para Saturno = {}" .format(floor(anosEmSat*365.25)))

print("Data terrestre para Saturno: {}" .format(dataInicial + time))