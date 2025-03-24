import smtplib
from email.mime.text import MIMEText
msg = MIMEText("Hello, this is a notification.")
msg["Subject"] = "Notification"
msg["From"] = "sender@example.com"
msg["To"] = "receiver@example.com"
with smtplib.SMTP("smtp.example.com") as server:
    server.send_message(msg)