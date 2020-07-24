#!/usr/bin/python3
# coding: utf-8
import mysql.connector
import time
import datetime
import os
import pipes
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
        self.row = [item[0] for item in db]
        for rem in remdb: # remove DB no needed
            self.row.remove(rem)

    def create_dump(self, backup_path):
        date_backup = time.strftime('%Y%m%d')
        for db_name in self.row:
            backup_day = backup_path + '/' + db_name
            try:
                os.stat(backup_day)
            except FileNotFoundError:
                os.system("mkdir -p " + backup_day)
            dump = "mysqldump -h localhost" + " -u " + self.user + " -p" + self.password + " " + db_name + " > " + pipes.quote(backup_day) + "/" + db_name + date_backup + ".sql"
            os.system(dump)
            zip = "gzip " + pipes.quote(backup_day) + "/" + db_name + date_backup + ".sql"
            os.system(zip)

def main():
    dbase = Database("root", '2Ksable$')
    dbase.show_database()
    dbase.create_dump('/home/backup')
    
if __name__ == "__main__":
    main()
