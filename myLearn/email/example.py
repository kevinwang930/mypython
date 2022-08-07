# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.

msg = EmailMessage()
msg.set_content("test email content")

me = "kevinwang930@hotmail.com"
you = "kevinwang930@hotmail.com"
msg['Subject'] = f'email subject'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost',1025)
s.send_message(msg)
s.quit()