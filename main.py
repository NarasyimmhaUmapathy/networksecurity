from networksecurity.entity.conf import DataIngestionConfig 
from networksecurity.entity.conf import TrainingPipelineConfig
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.logging.logging import logging
from networksecurity.entity.conf import DataIngestionConfig
from networksecurity.exceptions.exception import NetworkSecurityException
import sys 


if __name__=="__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("initiate data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    
    except Exception as e:
            raise NetworkSecurityException(e,sys)