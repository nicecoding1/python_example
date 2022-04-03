# ODBC 설정 방법
# https://blog.naver.com/oralol/222688258350

import pyodbc

server = "192.168.10.10"
user = "sys"
password = "tibero"
db = "tibero"
dsn = "tibero"

cnxn = pyodbc.connect('DSN='+dsn+';uid='+user+';pwd='+password)
cursor = cnxn.cursor()
cursor.execute("SELECT SYSDATE FROM DUAL")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()

cnxn.close()
