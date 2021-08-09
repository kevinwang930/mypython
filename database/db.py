# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 23:44:45 2020

@author: kevin
"""

import mysql.connector
from mysql.connector import errorcode
try:
    mydb = mysql.connector.MySQLConnection(
        host="localhost",
        port = 3310,
        user="kevin",
        passwd="123456",
        database="pharmacy"
        )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("mysql connection Somthing is wrong with your user name or password")
        raise SystemExit()
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("mysql connection Database does not exist")
        raise SystemExit()
    else:
        print(err)
else:
    mycursor = mydb.cursor()


def create_database(cursor, DB_name):
    try:
        cursor.execute(
            "create database {} default character set 'utf8'".format(DB_name))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
        


#mycursor.execute("create database pytest default character set 'utf8'")
#mycursor.execute("drop database pytest")

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x) 

# database="crashcourse"
# print("test print format {}".format(database))


