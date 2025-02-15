from collections import namedtuple

import pymongo
import pymongo.synchronous.mongo_client

client = pymongo.synchronous.MongoClient(host="mongodb", port=27017)

# Create a new client and connect to the server
#client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)