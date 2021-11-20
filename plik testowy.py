import time
# funkcja w funkcji z argumentami, sprawdzanie czasu działania programu.

def testF(func, arg,):
    start = time.perf_counter()
    func(arg)
    stop = time.perf_counter()
    wynikCzas = stop - start
    print('czas wykonywania : ', wynikCzas)

def dodawanie(a):
    for i in range(1000):
        a=a+1
    print(a)

def sumujParzyste(a=1,b=10):
    suma = 0
    for i in range(b-a+1):
        if i%2 == 0:
            suma=suma+i
    print(suma)

testF(dodawanie,500000)
testF(sumujParzyste,5)
