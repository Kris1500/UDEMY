import requests
workingList = []
notWorkingList = []
with open('www.txt', 'r') as file:
    for line in file:
        openWeb = requests.get(line)
        response = openWeb.status_code
        print(response)
        if response == 200:
            print('page is working, send to list"working" ')
            workingList.append(line)
        elif response == 404:
            print('page is not working, send to list "Not working" ')
            notWorkingList.append(line)
print('Working', workingList)
print('Not working', notWorkingList)