import mysql.connector
from mysql.connector import Error
import pandas as pd
import os

current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir,'Data','olist_order_payments_dataset.csv')
# order_payments = pd.read_csv(data_path)
# print(order_payments.head())

table_name = "olist_order_payments"


try:

    hostname = "yi-yd.h.filess.io"
    database = "ecommercesqldata_dideveryus"
    port = "3307"
    username = "ecommercesqldata_dideveryus"
    password = "8d8232a8c5d8a76f989b4490d9b50a0e14d99a69"


    connection = mysql.connector.connect(host=hostname,database=database,user=username,password=password,port=port)
    if connection.is_connected():
        db_info = connection.get_server_info()
        print('Connected to MySQL Server Version: ', db_info)
        
        # Creating a cursor to execute SQL queries
        cursor = connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS {table_name}")

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







