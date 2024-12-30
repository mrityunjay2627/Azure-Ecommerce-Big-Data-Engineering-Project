import mysql.connector
from mysql.connector import Error
import pandas as pd

hostname = "yi-yd.h.filess.io"
database = "ecommercesqldata_dideveryus"
port = "3307"
username = "ecommercesqldata_dideveryus"
password = "8d8232a8c5d8a76f989b4490d9b50a0e14d99a69"

try:
    connection = mysql.connector.connect(host=hostname,database=database,user=username,password=password,port=port)
    if connection.is_connected():
        db_info = connection.get_server_info()
        print('Connected to MySQL Server Version: ', db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Connected to database: ", record)

except Error as e:
    print("Error: ",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL Connection Closed')

