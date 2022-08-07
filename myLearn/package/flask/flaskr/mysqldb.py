# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 23:44:45 2020

@author: kevin
"""

import mysql.connector as mysqldb
from mysql.connector import errorcode

import click
from flask import current_app, g
from flask.cli import with_appcontext

config = {
    'host': '127.0.0.1',  # 连接的IP地址
    'user': 'kevin',
    'password': '123456',
    'port': 3310,
    'database': 'flask',
    'charset': 'utf8',  # 编码格式,防止查出来的数据中文乱码
}


def get_db():
    if 'db' not in g:
        try:
            g.db = mysqldb.connect(**config)
        except mysqldb.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("mysql connection Somthing is wrong with your user name or password")
                raise SystemExit()
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("mysql connection Database does not exist")
                raise SystemExit()
            else:
                print(err)
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
 

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        curs = db.cursor()
        for result in curs.execute('show grants;show databases;',multi= True):
            print(result.fetchall())
        cmd = f.read().decode('utf-8')
        
        for result in curs.execute(cmd,multi=True):
            pass

        curs.close()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
        

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    
    




