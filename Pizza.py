pizzaList=['A', 'B', 'C']

elementsA=['ser', 'cebula', 'sos']
elementsB=['ser', 'chrzan', 'czosnek']
elementsC=['se', 'pomidor', 'rukola']
sklA = {}
sklB = {}
sklC = {}

for a in elementsA:
    sklA[a] = 0
for b in elementsB:
    sklB[b] = 0
for c in elementsC:
    sklC[c] = 0

for i in pizzaList:
    print(i)
x = int(input('Wybierz pizze: (1,2 lub 3)'))

while True:
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

    if x != 1 or 2 or 3 or 0:
        break

print('pizzaA: ', sklA)
print('pizzaB: ', sklB)
print('pizzaC: ', sklC)