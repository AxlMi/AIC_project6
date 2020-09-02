#!/usr/bin/python3
# coding: utf-8
import mysql.connector
import os
import pipes
import var
import socket
import secure
import confidential
from sqlalchemy import create_engine


class Database:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.engine = create_engine('mysql+mysqlconnector://'+self.user+":"+self.password+"@localhost:3306", pool_recycle=3600)
    
    def show_database(self):
        """ This method will allow to create a list with the databases
        corresponding to my server"""
        remdb = ['information_schema', 'mysql', 'performance_schema','sys'] # DB that i do not want to back up
        db = self.engine.execute('SHOW DATABASES').fetchall()
        var.db_name = [item[0] for item in db]
        for rem in remdb: # remove DB no needed
            var.db_name.remove(rem)
        print(var.db_name)

    def create_dump(self, backup_path):
        """ this method will create the path to the dump,
        then she will create the dump ,
        and she will make an archive with gzip"""
        for db_name in var.db_name:
            new_backup_path = backup_path + '/' + db_name # path on my system for save before send to s3 
            var.path_list_s3.append('backup' + '/' + socket.gethostname() + '/' + db_name) # path to save on s3
            try:
                os.stat(new_backup_path)
            except FileNotFoundError:
                os.system("mkdir -p " + new_backup_path)
            dump = "mysqldump -h localhost" + " -u " + self.user + " -p" + self.password + " " + db_name + " > " + pipes.quote(new_backup_path) + "/" + db_name + var.today_date + ".sql"
            os.system(dump)
            secure.encrypt(pipes.quote(new_backup_path) + "/" + db_name + var.today_date + ".sql", confidential.key_encryption)
            zip = "gzip " + pipes.quote(new_backup_path) + "/" + db_name + var.today_date + ".sql"
            os.system(zip)
            

def main():
    dbase = Database("root", '2Ksable$')
    dbase.show_database()
    dbase.create_dump('/home/backup')
    sqlaws.create_fodler('projet6backup', var.path_list)


    print(var.path_list)
    
if __name__ == "__main__":
    main()
