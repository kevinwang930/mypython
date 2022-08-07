import mysql.connector as mysqldb
from mysql.connector import errorcode

config = {
    'host': '127.0.0.1',  # 连接的IP地址
    'user': 'kevin',
    'password': '123456',
    'port': '3310',
    'database': 'flask',
    'charset': 'utf8',  # 编码格式,防止查出来的数据中文乱码
}

def get_db_test():
    try:
        db = mysqldb.connect(**config)
    except mysqldb.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(
                "mysql connection Somthing is wrong with your user name or password")
            raise SystemExit()
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("mysql connection Database does not exist")
            raise SystemExit()
        else:
            print(err)
    mycursor = db.cursor()
    result = mycursor.execute('show databases;')
    print(result)
    for i in mycursor:
        print(i)
    print('test finished')


get_db_test()
