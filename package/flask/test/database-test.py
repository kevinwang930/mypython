import mysql.connector as mysqldb
from mysql.connector import errorcode

config = {
    'host': '127.0.0.1',  # 连接的IP地址
    'user': 'root',
    'password': '123456',
    'port': 3306,
    'database': 'flask',
    'charset': 'utf8',  # 编码格式,防止查出来的数据中文乱码
}

db = mysqldb.connect(**config)

curs =db.cursor()
curs.execute('show databases')
result = curs.fetchall()
print(result)
print(type(result))
