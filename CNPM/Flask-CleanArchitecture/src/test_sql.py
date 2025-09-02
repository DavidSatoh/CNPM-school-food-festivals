import pymssql

conn = pymssql.connect(
    server='127.0.0.1',
    user='sa',
    password='Aa123456', # Check this carefully!
    database='sql1'
)