import smtplib
#IMPORT SMTPLIB
#TO SEND EMAIL
smtpserver=smtplib.SMTP("smtp.gmail.com",587)
smtpserver.starttls()
#TO USE TLS
sender='tinaalex1307@gmail.com'
receiver='trishitagharai24@gmail.com'
password='jesuschrist13'
#LOGIN IN TO YOUR ACC
smtpserver.login(sender,password)
msg='HEY!'
smtpserver.sendmail(sender,receiver,msg)
print('YOUR MESSAGE HAS BEEN SENT')
smtpserver.close()