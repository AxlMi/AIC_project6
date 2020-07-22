#!/usr/bin/python3
# coding: utf-8
import mysql.connector
from sqlalchemy import create_engine


class Database:
    def __init__(self, user, password):
        self.engine = create_engine('mysql+mysqlconnector://'+user+":"+password+"@localhost:3306", pool_recycle=3600)
    
    def shdb(self):
        db = self.engine.execute('SHOW DATABASES')
        available_tables = db.fetchall()
        print(available_table)
    

def main():
    dbase = Database("root", '2ksable$')
    dbase.shdb
    
if __name__ == "__main__":
    main()
    print('test ok')