import pymysql
##from pymysql import *
conn=pymysql.connect(host='localhost', user='root',
                     passwd='', db='test')

cursor=conn.cursor()

cursor.execute('select * from usuarios')

for row in cursor:
    print(row)

cursor.close()
conn.close()

