import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import ssl

from email.message import EmailMessage


with open ('password.txt', 'r') as f:
    password=f.read()


# Define email sender and receiver
email_sender = 'giggyhadid3@gmail.com'
email_password = password
email_receiver = 'simpbean1069@gmail.com'

# Set the subject and body of the email
subject = 'Automation of mail sending using Python'
with open('message.txt', 'r') as f:
    message=f.read()
msg=MIMEMultipart()
msg.attach(MIMEText(message, 'plain'))

filename= 'pig.png'
attachment=open(filename, 'rb')

p=MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Diposition', f'attachment; filename={filename}')
msg.attach(p)




em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(msg)


# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())






