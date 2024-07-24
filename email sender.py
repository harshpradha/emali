import smtplib
server=smtplib.SMTP(host='smtp.gmail.com',port=587)
server.starttls() start the server

receiver_email=input('Enter your email💕')
sender_email="harshpradhan936@gmail.com"
sender_password='uzrr lncf pmkt odym'
server.login(sender_email,sender_password)
subject=input("what is your problem 🤦‍♀️")
body=input("bhai kucch to bol muhh to khol")
message=f'subject: {subject}\n\n{body}'
server.sendmail(sender_email,receiver_email,message)
print('aap ka  email ka jugaad ho gya ')
server.quit()





smpt library= server ka kaam karta h ()
