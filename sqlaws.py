#!/usr/bin/python3
# coding: utf-8
import boto3
import var
import confidential
import socket
import secure
import os


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

def export_dump():
    name_server = input("Quel est le nom du serveur sur lequel est la base de donnée ? ")
    name_bdd = input("Quel est le nom de la base de donnée ? ")
    date_ok = False
    while not date_ok:
        try:
            year_bdd = int(input("A quelle annee souhaitez vous faire la restauration ? "))
            if year_bdd <= 2000 or year_bdd > 2100:
                print("Entrez une année correcte")
            else:
                month_bdd = int(input("A quel mois souhaitez vous faire la restauration ? "))
                if month_bdd > 12:
                    print("Merci d'indiquez un mois compris entre 01 et 12")
                else:
                    day_bdd = int(input("A quel jour souhaitez vous faire la restauration ? "))
                    if day_bdd > 0 and day_bdd < 31:
                        date_ok = True
                    else:
                        print("merci d'indiquez un jour compris entre 1 et 31")
        except:
            print("Merci d'indiquer une date correcte")

    if month_bdd < 10:
        month_bdd = "0"+str(+month_bdd)
    else:
        month_bdd = str(month_bdd)

    if day_bdd < 10:
        day_bdd = "0"+str(+day_bdd)
    else:
        day_bdd = str(day_bdd)

    year_bdd = str(year_bdd)
    
    name_restore = name_bdd+year_bdd+month_bdd+day_bdd+".sql.gz"
    path = "backup/"+name_server+"/"+name_bdd+"/"+name_restore
    try:
        s3.download_file("projet6backup", path, name_restore)
        os.system("gzip -d "+name_restore)
        secure.decrypt(name_bdd+year_bdd+month_bdd+day_bdd+".sql", confidential.key_encryption)
    except Exception as e:
        print(e, "êtes vous sur que le fichier existe ?")

def main():
    export_dump()
    
if __name__ == "__main__":
    main()