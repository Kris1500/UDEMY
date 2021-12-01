import time
import datetime
import smtplib
prod1=0
prod2=0
listEnd=[]
tekst='hello'
while True:
 x=int(input('Wybierz pizze: 1- serowa, 2- wege \n'))
 if x==1:
  #dict.update({1:1})
  prod1+=1
  print('pizza zapisana!\n ')
  print('Aktualny stan zamowien: \n pizza serowa: ', prod1, '\n pizza wege: ', prod2, '\n')
  time.sleep(1)
 if x ==2:
  prod2+=1
  print('pizza zapisana!')
  print('Aktualny stan zamowien: \n pizza serowa: ', prod1, '\n pizza wege: ', prod2, '\n')
  time.sleep(1)
 if x ==3:
  break
xDic=[]
pizza1=('ser', 'mleko', 'kielbasa', 'szynka')
pizza2=('ser', 'oliwki', 'ananas')
x=prod1*pizza1
x2=prod2*pizza2
xAll=x+x2
listaK=[]
for elements in xAll:
    xAllList=(elements, xAll.count(elements))
    listaK+=xAllList

listEnd=str(listaK)
print(listEnd)
czas = datetime.datetime.now()
file = open(r'C:\Users\Milka\PycharmProjects\UDEMY\car.txt', 'a')
file.write('Witaj, to lista składników wykorzystanych dziś:')
file.write('\n')
file.write(str(czas))
file.write('\n')
file.write(listEnd)
file.write('\n')

#file.close()

#file2 = open(r'C:\Users\Milka\PycharmProjects\UDEMY\car.txt', 'a')
#tekst=file.read()
#print(tekst)


mailFrom = 'jk.workplace@gmail.com'
mailTo = 'ciesielski.kris@gmail.com'
mailSubject = 'Pizzeria'
mailBody = listEnd


message = '''From: {}
Subject: {}

{}
'''.format(mailFrom, mailSubject, mailBody)
user = 'jk.workplace@gmail.com'
password = 'milusia06'
try:
    server = smtplib.SMTP_SSL('Smtp.gmail.com', 465)
    print(server.ehlo())
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending mail')
