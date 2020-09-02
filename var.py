#!/usr/bin/python3
# coding: utf-8
import time
import socket

path_list_s3 = []

path_dump = '/home/backup'

bucket_name = 'projet6backup'

db_name = []

today_date = time.strftime('%Y%m%d') # date of the day

backup_path = ''

smtp_sujet = "Rapport backup mysql serveur : " + socket.gethostname()

smtp_message_ok = "Bonjour, votre sauvegarde du serveur : "

