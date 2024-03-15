# Get the database using the method we defined in pymongo_test_insert file
from io import StringIO
from pymongo_get_database import get_database
from dateutil import parser
import pandas as pd
import numpy as np

dbname = get_database()
print()
collection_name = dbname['User']

user_detail = pd.read_csv('../data/user_df.csv')
user_detail.head(4)


# Convert DataFrame to list of dictionaries
data_dict = user_detail.to_dict(orient='records')

# Insert data into MongoDB
collection_name.insert_many(data_dict)

# Confirm insertion
print("Data inserted successfully.")











