import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "muddassarhussain90@gmail.com"
password = "zgrezriwoezcdbgr"


receiver_email = "mudasarawan08@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
How are You ? 
Hope You are well ?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver_email, message)
