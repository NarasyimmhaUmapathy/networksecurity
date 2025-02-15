
import os
import sys
import json 
import certifi,pandas as pd
from networksecurity.exceptions.exception import NetworkSecurityException
from networksecurity.logging.logging import logging

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")

ca = certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection 
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__="__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="KRISHAI"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records = networkobj.json_convertor(file_path=FILE_PATH)
    no_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)

    print(no_records)
