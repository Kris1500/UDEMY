import random
import pomocniczy
bazaBroni=[['łuki', 15, 45], ['siekiera', 35, 65], ['miecz', 65, 75], ['nóż', 85, 55]]

# ilość trafień z broni
# 1 - łuk, 2- siekiera, 3- miecz, 4 - nóz
bron = {'łuk': 15, 'siekiera': 35, 'miecz': 65, 'nóż': 85, }
bron2 = {'łuk': 45, 'siekiera': 65, 'miecz': 75, 'nóż': 55, }
'''
listaBroni = [sztuka        #  wyrażenie listowe
              for sztuka in bazaBroni
              for sztuka1 in sztuka
                                          ]
print(listaBroni) 
'''
print('Oto nasza dostępna broń: ', list(bron))
a=int(input('Podaj skuteczność trafień broni( w % ) która Cię interesuje: '))
print('Dostępna broń i jej skuteczność trafień')
for k,v in bron.items():
    if v > a:
        print(k,v)
bronAnaliza = input('wybierz broń do analizy, podaj jej nazwę: ')
if bronAnaliza == 'łuk':
    pomocniczy.procS(bazaBroni[0][1],bazaBroni[0][2])

elif bronAnaliza == 'siekiera':
    pomocniczy.procS(bazaBroni[1][1],bazaBroni[1][2])

elif bronAnaliza == 'miecz':
    pomocniczy.procS(bazaBroni[2][1],bazaBroni[2][2])

elif bronAnaliza == 'nóż':
    pomocniczy.procS(bazaBroni[3][1],bazaBroni[3][2])