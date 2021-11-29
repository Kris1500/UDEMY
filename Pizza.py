pizzaList=['A', 'B', 'C']

elementsA=['ser', 'cebula', 'sos']
elementsB=['ser', 'chrzan', 'czosnek']
elementsC=['ser', 'pomidor', 'rukola']
sklA = {}
sklB = {}
sklC = {}
listaW=[0, 1, 2, 3]
#slownik = {sklA, sklB}

for a in elementsA:
    sklA[a] = 0
for b in elementsB:
    sklB[b] = 0
for c in elementsC:
    sklC[c] = 0

for i in pizzaList:
    print(i)


while True:
    try:
        x = int(input('Wybierz pizze: (1,2 lub 3)'))
    except ValueError:
        print('podaj liczbę!')
        continue
    if x == 1:
        for a in elementsA:
            sklA[a] += 1

    if x == 2:
        for b in elementsB:
            sklB[b]+=1
    if x == 3:
        for c in elementsC:
            sklC[c]+=1
    if x == 0:
        break

    if x not in listaW:
        print('pomyliłeś numerek!')
        continue

print('pizzaA: ', sklA)
print('pizzaB: ', sklB)
print('pizzaC: ', sklC)

print(slownik)

