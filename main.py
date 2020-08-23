#!/usr/bin/python3
# coding: utf-8
import sqlsave
import sqlaws
import var
import confidential
import os



dbase = sqlsave.Database(confidential.sql_user, confidential.sql_password)
dbase.show_database()
dbase.create_dump(var.path_dump)
sqlaws.create_folder(var.bucket_name, var.path_list_s3)
sqlaws.import_dump()
os.system("rm -rf /home/backup")

