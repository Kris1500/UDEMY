import random
bazaBroni=[['łuk', 15, 45], ['siekiera', 35, 65], ['miecz', 65, 75], ['nóż', 85, 55]]
def ciosy(pr):
    if pr < random.randint(0, 100):
        print('hit')
    else:
        print('not hit')

# ilość trafień z broni
# 1 - łuk, 2- siekiera, 3- miecz, 4 - nóz
bron = {'łuk': 15, 'siekiera': 35, 'miecz': 65, 'nóż': 85, }
bron2 = {'łuk': 45, 'siekiera': 65, 'miecz': 75, 'nóż': 55, }
#bron2 = {'łuk'=[15,35], siekiera = {35,85}, {miecz = 65,65}, nóż = {85,45}}
#print(bron2)
listaBroni = {sztuka        #  wyrażenie listowe
              for sztuka in bron
              }
print('Oto nasza dostępna broń: ')
print(list(bron))
a=int(input('Podaj skuteczność trafień broni( w % ) która Cię interesuje: '))
print('Dostępna broń i jej skuteczność trafień')
for k,v in bron.items():
    if v > a:
        print(k,v)
print('wybierz broń do analizy')
bronAnaliza = input('podaj nazwę: ')
if bronAnaliza == 'łuk':
    print('doskonały wybór!')
    print('Aby unicestwić rywala w 100 % musisz wykonać')# %s strzałów', %) #popraw %
    for k,v in bron2.items():
        if k == bronAnaliza:
            print(k, 'ma śmiertelnosc ciosów: ', v, '%')

bazaStrzałów = []
i = 0

while i<=3:
    i+=1
    ciosy(bazaBroni[0][1])
bazaStrzałów.append(ciosy(bazaBroni[0][1]))
from collections import Counter
print(Counter(bazaStrzałów))

