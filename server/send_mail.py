import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import username, password

def send_mail(to_addresses, to_name, subject, content):

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = username
    message['To'] = to_name
    message['Subject'] = subject
    #The body and the attachments for the mail
    message.attach(MIMEText(content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(username, password) #login with mail_id and password
    text = message.as_string()
    session.sendmail(username, to_addresses, text)
    session.quit()

    print('Mail Sent to', to_addresses, to_name)
