# Get the database using the method we defined in pymongo_test_insert file
from io import StringIO
# from pymongo_get_database import get_database
from pymongo.mongo_client import MongoClient
# from dateutil import parser
import pandas as pd
import numpy as np


def get_database():
   cluster = MongoClient("mongodb+srv://new_user_1:new_user_1@autobasket.rbhfxd5.mongodb.net/?retryWrites=true&w=majority&appName=AutoBasket")
   db = cluster['Autobasket']
#    collection = db['User']
   return db

dbname = get_database()
collection_name = dbname['User']
print(collection_name)

def read_csv():
    user_detail = pd.read_csv('../data/user_df.csv')
    print(user_detail.head(4))


def insert_user_detail():
    user_detail= read_csv()
    # Convert DataFrame to list of dictionaries
    data_dict = user_detail.to_dict(orient='records')

    # Insert data into MongoDB
    collection_name.insert_many(data_dict)

    # Confirm insertion
    print("Data inserted successfully.")

def get_data_from_DB():
    # cursor = collection_name.find()
    # for document in cursor:
    #     print(document)
    try:   
        x = collection_name.find_one()
        print(x)
    except Exception as e:
      print(e)

# get_data_from_DB()
def insert_one_user_detail():
    user_one = {'User ID' : 10007 ,'User Name' :  'hb' ,'User Email' :'hb.gmail.com'  ,'User Age' :7}
    result = collection_name.insert_one(user_one)
    print(result)
    return result
    
# result = insert_one_user_detail()
# print(result)

get_data_from_DB()
    










