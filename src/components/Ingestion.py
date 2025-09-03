import os
import sys
import pandas as pd
from src.entity.config_entity import DataIngestionConfig
from src import customException
from src import get_logger
from src.utils.common import create_directories

logging = get_logger()

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self):
        try:
            # Read the raw data CSV
            p = "../../notebook/BMW_Car_Sales_Classification.csv"
            df = pd.read_csv(p)
            logging.info(f"Read data from {p } with shape {df.shape}")

            # Create root directory if it doesn't exist
            create_directories([self.config.root_dir])
            logging.info(f"Created directory at {self.config.root_dir}")

            #save in path artifact from my data
            df.to_csv(self.config.local_data_file,index=False)
            logging.info(f"Saved raw data to {self.config.local_data_file}")
        
        except Exception as e:
            logging.error("Error in data ingestion")
            raise customException(e, sys)