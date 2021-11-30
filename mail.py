import smtplib
mailFrom = 'jk.workplace@gmail.com'
mailTo = 'ciesielski.kris@gmail.com'
mailSubject = 'Test -  message'
mailBody = '''Hello
everything is fine! ciao'''

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

