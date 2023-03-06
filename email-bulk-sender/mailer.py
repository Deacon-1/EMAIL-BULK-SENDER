import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP server configuration
smtp_host = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email@gmail.com'
smtp_password = 'your_email_password'

# Email content
subject = 'Subject line of the email'
body = 'Body of the email'

# Email list
email_list = ['email1@example.com', 'email2@example.com', 'email3@example.com']

# Create a message object
message = MIMEMultipart()
message['From'] = smtp_username
message['Subject'] = subject

# Attach the message body
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server
smtp_server = smtplib.SMTP(smtp_host, smtp_port)
smtp_server.starttls()
smtp_server.login(smtp_username, smtp_password)

# Send emails to the list of recipients
for email in email_list:
    message['To'] = email
    smtp_server.sendmail(smtp_username, email, message.as_string())

# Close the SMTP server connection
smtp_server.quit()
