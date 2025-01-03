from pymongo import MongoClient
import pandas as pd
import os

hostname = "4ty9e.h.filess.io"
database = "ecommercenosqldata_saltreadon"
port = "27018"
username = "ecommercenosqldata_saltreadon"
password = "71191818a120692542519aeab29b017f066b430e"

uri = "mongodb://" + username + ":" + password + "@" + hostname + ":" + port + "/" + database

try:
    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir,'Data','product_category_name_translation.csv')
    product_category_df = pd.read_csv(data_path)
except FileNotFoundError:
    print("File Not Found!")
    exit()

try:
    client = MongoClient(uri)
    database = client[database]

    # Select the collection (or create if doesn't exists)
    collection = database["Product Categories"] # Suitable Name for our collection

    # Dataframe to list of dictioanries to insert in MongoDB database
    data_to_insert = product_category_df.to_dict(orient="records")

    # Insert data into the collection
    collection.insert_many(data_to_insert)    

    print("Data Uploaded to MongoDB successfully")

except Exception as e:
    print("Error occured: {e}")

finally:
    if client:
        client.close()

