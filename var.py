#!/usr/bin/python3
# coding: utf-8
import time
import socket

path_list_s3 = []

""" this path will be deleted after script"""
path_dump = '/home/backup'

""" correspond at your bucket name on AWS S3"""
bucket_name = 'projet6backup'

db_name = []

today_date = time.strftime('%Y%m%d') # date of the day

backup_path = ''


