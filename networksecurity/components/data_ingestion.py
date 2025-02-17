from networksecurity.exceptions.exception import NetworkSecurityException
from networksecurity.logging.logging import logging 

from networksecurity.entity.conf import DataIngestionConfig 
from networksecurity.entity.artifact_entity import DataIngestionArtifact
import os,sys
import pymongo 
import pandas as pd
import numpy as np
from typing import List 


from dotenv import load_dotenv
load_dotenv()

mongo_db_url = os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = DataIngestionConfig()
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def read_collection(self):
        try: 
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client"pymongo.MongoClient(MONGO_DB_URL)"
            collection = "self.mongo_client[database][collection_name]"
       
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"],axis=1)

            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityException



        
    def export_data_to_feast(self,dataframe:pd.DataFrame):
        #feature store functionality
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dataframe=self.data_ingestion_config.feature_store_file_path
            #create folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    
    def initiate_data_ingestion(self):
        df = self.read_collection() 
        df = self.export_data_to_feast(df)
        self.train_test_split(df)
        dataingestionartifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                                      test_file_path=self.data_ingestion_config.test_file_path
                                                )
        return dataingestionartifact

    def train_test_split(self,df:pd.DataFrame):

        #train test split
        logging.info("splitting dataset to train and test")

        dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)

        os.makedirs(dir_path,exist_ok=True)

        logging.info("export data to train and test csv")

        #train_set.to_csv(
         #   self.data_ingestion_config.training_file_path,index=False,header=True)
        
        #)

        #test_set.to_csv(
        #   self.data_ingestion_config.test_file_path,index=False,header=True)

        #

        logging.info("exported data")
