#!/usr/bin/python3
# coding: utf-8
import sqlsave
import sqlaws
import var
import confidential
import os
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import socket

msg = MIMEMultipart()

msg['From'] = confidential.fromaddr
msg['To'] = confidential.toaddrs

msg['Subject'] = 'Backup SQL to AWS'

server = smtplib.SMTP("smtp.gmail.com", 587)
server.connect(confidential.smtp_server, confidential.smtp_port)
server.ehlo()
server.starttls()
server.login(confidential.user_smtp, confidential.password_smtp)
fromaddr = confidential.fromaddr
toaddrs = confidential.toaddrs

try:   
    dbase = sqlsave.Database(confidential.sql_user, confidential.sql_password)
    dbase.show_database()
    dbase.create_dump(var.path_dump)
    sqlaws.create_folder(var.bucket_name, var.path_list_s3)
    sqlaws.import_dump()
    try:
        name = socket.gethostname()
        messages = MIMEText('Bonjour,\nla sauvegarde du {} concernant le serveur {} à fonctionné'.format(var.today_date, name))
        msg.attach(messages)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
    except Exception as err:
        print(err)
except Exception as exc:
    name = socket.gethostname()
    messages = MIMEText("Bonjour,\n\nla sauvegarde du {} concernant le serveur {} à rencontré l'erreur suivante :\n{}".format(var.today_date, name, exc))
    msg.attach(messages)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    print("une erreur", exc)
os.system("rm -rf /home/backup")



