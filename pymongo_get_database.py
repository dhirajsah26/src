# from pymongo import MongoClient
from pymongo.mongo_client import MongoClient

def get_database():
   cluster = MongoClient("mongodb+srv://new_user_1:new_user_1@autobasket.rbhfxd5.mongodb.net/?retryWrites=true&w=majority&appName=AutoBasket")
   db = cluster['Autobasket']
   collection = db['User']
   return db

   print(collection.getName())
   # # Create a document to insert
   # user_data = {
   #    "username": "example_user",
   #    "email": "example@example.com",
   #    "age": 30
   # }
   # # Insert the document into the collection
   # result = collection.insert_one(user_data)
   # # Check if the insertion was successful
   # if result.inserted_id:
   #    print("Document inserted successfully with ID:", result.inserted_id)
   # else:
   #    print("Failed to insert document")
   #    # Send a ping to confirm a successful connection
   # try:
   #    client.admin.command('ping')
   #    print("Pinged your deployment. You successfully connected to MongoDB!")
   #    return client['autobasket']
   # except Exception as e:
   #    # print("failed"+ "-_______________________"*40)
   #    print(e)
   # # Create the database for our example (we will use the same database throughout the tutorial
 
  
# This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":   
  
   # Get the database
# get_database()