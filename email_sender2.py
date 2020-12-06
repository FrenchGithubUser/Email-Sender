from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time


# create message object instance
msg = MIMEMultipart()

def get_message(message_file):
    with open(message_file) as texte:
        message = texte.read()
    return message

def get_emails(emails_file):
    email_list = []
    file1 = open(emails_file, "r")
    while(True):
    	line = file1.readline()
    	if not line:
    		break
    	email_list.append(line.strip())
    file1.close()
    return email_list

message = get_message('message.txt')
emails = get_emails('emails.txt')

# setup the parameters of the message
password = "password"
msg['From'] = "your@email.here"

msg['Subject'] = "subject"

# add in the message body
msg.attach(MIMEText(message))

server = smtplib.SMTP('smtp-mail.outlook.com: 587')
server.starttls()
server.login(msg['From'], password)

number = 0

for email in emails:
    try:
        server.sendmail(msg['From'], email, msg.as_string())
        print(f'Email sent to {email}')
        time.sleep(1)
    except:
        time.sleep(60)
        server.sendmail(msg['From'], email, msg.as_string())
        print(f'Email sent to {email}')
    number += 1
server.quit()

print(f'{number} emails sent !')
