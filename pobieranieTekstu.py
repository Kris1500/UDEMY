name = []   # empty list
with open('imieNazwisko.txt', 'r') as file:     # open exist file txt
    for line in file:
        name.append(tuple(line.replace('\n', '').split(' '))) # add to list
    print(name)
with open('imie.txt', 'w') as file:     # new txt file
    for item in name:
        file.write(item[0]+'\n')        #save new txt file with results
