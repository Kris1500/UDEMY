name = []   # pusta baza
with open('imieNazwisko.txt', 'r') as file:     # otwiera istniejący plik
    for line in file:
        name.append(tuple(line.replace('\n', '').split(' '))) # tworzy listę krotek
    print(name)
with open('imie.txt', 'w') as file:     #tworzy nowy plik tesktowy
    for item in name:
        file.write(item[0]+'\n')        #dla kazdej krotki w liscie wybiera pierwszy element i zapisuje
