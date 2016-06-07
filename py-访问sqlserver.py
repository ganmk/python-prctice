#访问SqlServer

import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.1.100\\sql;DATABASE=testDB;UID=sa;PWD=myPassword')

cursor = cnxn.cursor()

cursor.execute("select * from Tb")
