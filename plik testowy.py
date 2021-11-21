import time
#  bfunkcja w funkcji z argumentami, sprawdzanie czasu działania programu.

def testF(func, arg,):
    start = time.perf_counter()
    func(arg)
    stop = time.perf_counter()
    wynikCzas = stop - start
    print('czas wykonywania : ', wynikCzas)

def dodawanie(c,d=11):
    a = 0
    for i in range(c,d):
        a=a+i
    print(a)

def sumujParzyste(a=1,b=10):
    suma = 0
    for i in range(b-a+1):
        if i%2 == 0:
            suma=suma+i
    print(suma)

testF(dodawanie,1)
testF(sumujParzyste,5)
