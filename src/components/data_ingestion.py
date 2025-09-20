import os  
import sys 
from src.exception import CustomException 
from src.logger import logging 
import pandas as pd 
from dataclasses import dataclass 
from sklearn.model_selection import train_test_split 


@dataclass 
class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts", "data.csv")
    train_data_path:str = os.path.join("artifacts", "train.csv")
    test_data_path:str = os.path.join("artifacts", "test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            df = pd.read_csv(r"C:\Users\hp\Files\DataScience\End-To-End Projects\ML_project\data\stud.csv")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False , header=True)

            logging.info("Train test split intialized")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Spliting Done.")


        except Exception as e:
            raise CustomException(e, sys)
        

if __name__=="__main__":
    obj = DataIngestion() 
    obj.initiate_data_ingestion()