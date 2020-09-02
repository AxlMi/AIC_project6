#!/usr/bin/python3
# coding: utf-8
import boto3
import var
import confidential
import socket

s3 = boto3.client('s3',
                    aws_access_key_id=confidential.aws_key,
                    aws_secret_access_key=confidential.aws_secret)


def create_folder(bucket_name, path):
    for x in path:
        print(x)
        s3.put_object(Bucket=bucket_name, Key=(x+'/'))


def import_dump():
    for db in var.db_name:
        path_host = var.path_dump + "/" + db + '/' + db+var.today_date + '.sql' + '.gz'
        path_s3 = 'backup' + '/' + socket.gethostname() + '/' + db + '/' + db+var.today_date + '.sql' + '.gz' # path to save on s3
        s3.upload_file(path_host, var.bucket_name, path_s3)

def export_dump(name_server, dl_db, date_of_db):
    path = var.path_dump + "/" + dl_db + "/" + dl_db+date_of_db+'.sql.gz'
    s3.download_file(var.bucket_name, path, "/home")
    

