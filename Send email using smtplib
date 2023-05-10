import smtplib, ssl
from email.mime.text import MIMEText

speed=float(input("Kindly enter the Mbps value in Mbps\n"))
#1 Mbps =  .125 MBps
MBps = float(.125*speed)
message = f"The MBps value is {MBps}, your Mbps value {speed}"



server = smtplib.SMTP_SSL(host='smtp.gmail.com', port='465')


a=["vignesh8458@gmail.com", "mdeepak1509@gmail.com"]


server.login(user="vignesh8458@gmail.com", password="ngsgvjacjnftwwbd")
server.sendmail(from_addr="vignesh8458@gmail.com", to_addrs=a, msg=message)

print(message)
