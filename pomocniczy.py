import random
#ile strzałów trzeba oddać by osiągnąć 100 %
def procS(prS):
    listaS =[]
    a = prS
    i = 0
    while a < 101:
        a+=prS
        i+=1
    print('dla 100% skuteczności potrzba ', i, 'celnych strzałów')
    listaS.append(i)
    print(listaS,'lista')
    print(prS, 'zalozenie procentowe')
    j = 0
    l = 0
    while j < listaS[0]:
        if prS > random.randint(0,100):
                l+=1
                j+=1
                print('j rosnie', j)
        else:
                l+=1
                j=j
                print('bez zmian', j)
    print(l, 'to jest to')

procS(10)
