#!/usr/bin/python3
# coding: utf-8
import confidential
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
import var

msg = MIMEMultipart()

msg['From'] = confidential.fromaddr
msg['To'] = confidential.toaddrs

msg['Subject'] = 'Backup SQL to AWS'
server = smtplib.SMTP(confidential.smtp_server, confidential.smtp_port)
server.connect(confidential.smtp_server, confidential.smtp_port)
server.ehlo()
server.starttls()
server.login(confidential.user_smtp, confidential.password_smtp)
fromaddr = confidential.fromaddr
toaddrs = confidential.toaddrs
name = socket.gethostname()

def send_ok():
    messages = MIMEText('Bonjour,\nla sauvegarde du {} concernant le serveur {} à fonctionné'.format(var.today_date, name))
    msg.attach(messages)
    server.sendmail(fromaddr, toaddrs, msg.as_string())

def send_err(error,):
    messages = MIMEText("Bonjour,\n\nla sauvegarde du {} concernant le serveur {} à rencontré l'erreur suivante :\n{}".format(var.today_date, name, error))
    msg.attach(messages)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
