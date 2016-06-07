#!/usr/bin/env python
# --*-- coding:utf-8 --*--

import MySQLdb  #操作mysql，需要加载MySQLdb模块

#创建连接
conn = MySQLdb.connect(host = '127.0.0.1',user = 'root',passwd = '123',db = 'mydb')     #使用connect方法对数据库进行连接，相当于一个门
cur = conn.cursor()     #使用conn.cursor方法，相当于操作的一双手

#操作数据库
reCount = cur.execute('select * from students')     #可以看到主函数的操作是查看students表
table = cur.fetchall()                       #将操作所得到的数据全部拿出来         #

#关闭连接
cur.close()             #结束操作后，将手拿回来
conn.close()            #将门关上
print reCount      #cur.execute返回的是操作影响的行数
print data         
