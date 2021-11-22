import requests
listaDz = []
listaNdz = []
with open('www.txt', 'r') as file:
    for line in file:
        openWeb = requests.get(line)
        response = openWeb.status_code
        print(response)
        if response == 200:
            print('strona działa, zostaje dodana do listy stron działających')
            listaDz.append(line)
        elif response == 404:
            print('strona nie działa, zostaje dodana do listy zablokowanych')
            listaNdz.append(line)
print('Działa', listaDz)
print('Nie działa', listaNdz)