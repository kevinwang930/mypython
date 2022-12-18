# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Open the plain text file whose name is in textfile for reading.

msg = MIMEMultipart('alternative')


me = "kevinwang930@hotmail.com"
you = "kevinwang09@foxmail.com"
msg['Subject'] = f'report-email'
msg['From'] = me
msg['To'] = you

html = '''
<html>
    <body>
        Hello, this is a html email!
    </body>
</html>
'''
html_body = MIMEText(html,'html')
msg.attach(html_body)

# Send the message via our own SMTP server.
s = smtplib.SMTP("smtp-mail.outlook.com",587)
s.ehlo()
s.starttls()
s.login("kevinwang930@hotmail.com","1134824458wang")
s.send_message(msg)
s.quit()

