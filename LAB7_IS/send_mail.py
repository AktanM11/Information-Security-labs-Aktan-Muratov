#!/usr/bin/env python3
import smtplib
import socket
from datetime import datetime
from email.message import EmailMessage

SMTP_HOST = "smtp.postmarkapp.com"
SMTP_PORT = 587
SMTP_USER = ""
SMTP_PASS = ""

SENDER = "ma13248@auca.kg"
RECEIVER = "ma13248@auca.kg"

msg = EmailMessage()
msg["Subject"] = f"Cron report from {socket.gethostname()}"
msg["From"] = SENDER
msg["To"] = RECEIVER
msg.set_content(f"Server is alive. Time: {datetime.now()}")

with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
    smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASS)
    smtp.send_message(msg)

print(f"{datetime.now()} - email sent")