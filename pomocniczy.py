import random
#ile strzałów trzeba oddać by osiągnąć 100 % skutecznosci
def procS(prS, prT=100):
    listaS =[]  #lista strzałów
    a = prS
    i = 0

    while a < 101:
        a+=prS
        i+=1
    if prS > 49:
        i=i+1
    print('dla', prS, '% zadania ran, dla 100% skuteczności wyeliminowania rywala potrzba ', i, 'celnych strzałów')
    listaS.append(prT)
    listaS.append(i)

    j = 0
    l = 0

    while j < listaS[1]:
        if prS >= random.randint(0,100):
                l+=1
                j+=1
                #print('j rosnie', j)
        else:
                l+=1
                j=j
                #print('bez zmian', j)
    print('aby to osiągnąć, przy', prT, ' % współczyniku trafień, nalezy oddać', l, 'strzałów')
#procS(60,60)