from datetime import datetime
import os
from networksecurity.constants import training_pipeline


class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = training_pipeline.pipeline_name
        self.artifact_dir = training_pipeline.artifact_dir
        self.timestamp: str =timestamp

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,training_pipeline.data_ingestion_dir_name
        )
        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir,training_pipeline.data_ingestion_feature_store
        )
        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir,training_pipeline.data_engestion_ingested_dir,training_pipeline.train_file_name
        )
        self.test_file_path: str = os.path.join(
            self.data_ingestion_dir,training_pipeline.data_engestion_ingested_dir,training_pipeline.test_file_name
        )

        self.train_test_split_ratio : float = training_pipeline.data_ingestion_train_test_split_ratio
        self.collection_name : str = training_pipeline.data_ingestion_collection_name
        self.database_name : str = training_pipeline.data_ingestion_db_name

