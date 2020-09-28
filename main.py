#!/usr/bin/python3
# coding: utf-8
import sqlsave
import sqlaws
import var
import confidential
import os
import time
import create_crontab
import send_mail

# if all goes well, I will send an email to indicate the correct execution of the script
try:
    # instantiate DB
    dbase = sqlsave.Database(confidential.sql_user, confidential.sql_password)
    # function to save all data base in the variable 'var.db_name'
    dbase.show_database()
    # will create dump for all DB in the variable var.db_name , zip him and save the path on var.path_list_s3
    dbase.create_dump(var.path_dump)
    # get the variable var.path_list_s3 for create structure on S3
    sqlaws.create_folder(var.bucket_name, var.path_list_s3)
    # take the var.db_name and import all DUMP create on AWS S3
    sqlaws.import_dump()
    try:
        send_mail.send_ok()
    except Exception as err:
        print(err)
# if I encounter an error, I send an email indicating the error encountered
except Exception as exc:
    send_mail.send_err(exc)
    print("une erreur", exc)
""" need to delete the dump created previously"""
os.system("rm -rf /home/backup")

""" the first variable correspond at ur user and the second at the time of execution cron"""
create_crontab.create_cron("root", 23)


