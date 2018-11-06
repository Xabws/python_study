# -*- coding: UTF-8 -*-
import MySQLdb

"""
数据库url，用户名和密码，数据库名称，编码版本
conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="test",charset="utf8")  
cursor = conn.cursor()    
"""


class Dbtest:
    def exedb(self):
        db = MySQLdb.connect("localhost", "root", "1234", "test")
        cursor = db.cursor();
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取一条数据库。
        data = cursor.fetchone()
        print ("Database version : %s " % data)
        # 关闭数据库连接
        db.close()

dbtest =Dbtest();
dbtest.exedb();