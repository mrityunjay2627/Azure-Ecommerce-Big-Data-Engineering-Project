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

        cursor.execute(f"DROP TABLE IF EXISTS {table_name};")

        create_table_query = f"""
        CREATE TABLE {table_name} (
            order_id VARCHAR(50),
            payment_sequential INT,
            payment_type VARCHAR(20),
            payment_installments INT,
            payment_value FLOAT
        );
        """
        

        cursor.execute(create_table_query)
        print(f"Table `{table_name}` created successfully!")

        order_payments_data = pd.read_csv(data_path)
        print('CSV data loaded into pandas Dataframe.')

        # Insert data in batches
        batch_size = 500
        total_records = len(order_payments_data)

        print('\n Data Insertion in batches begin\n')

        for start in range(0, total_records, batch_size):
            end = start + batch_size

            batch = order_payments_data.iloc[start:end]

            # Convert batch to list of tuples for MySQL insertion
            batch_record = [
                tuple(row) for row in batch.itertuples(index=False, name=None)
            ]

            # INSERT Query
            insert_query = f"""
            INSERT INTO {table_name}
            (order_id, payment_sequential, payment_type, payment_installments, payment_value)
            VALUES
            (%s, %s, %s, %s, %s) 
            """

            # Inserion Query Execution after each batch
            cursor.executemany(insert_query, batch_record)
            connection.commit() # Commit after each batch
            print(f"Inserted {start+1} to {end} records")
        
        print('\nAll records inserted successfully!\n')

except Error as e:
    print("Error: ",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL Connection Closed')







