import os  
import sys 
from src.exception import CustomException
from src.logger import logging 
import pandas as pd 
from dataclasses import dataclass 
from sklearn.model_selection import train_test_split 

from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


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
            df = pd.read_csv(r"data\stud.csv")
            logging.info(f"dataset consist of {df.shape[0]} row and {df.shape[1]} feature.")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False , header=True)
            logging.info(f"raw data saved into {self.ingestion_config.raw_data_path}")

            logging.info("Train test split intialized")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info(f"shape of train data {train_set.shape} and shape of test data {test_set.shape}")

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info(f"train saved into -> {self.ingestion_config.train_data_path} ")
            logging.info(f"test saved into -> {self.ingestion_config.test_data_path} ")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e, sys)
        


if __name__ == "__main__":
    obj = DataIngestion() 
    train_data , test_data = obj.initiate_data_ingestion() 

    data_transformation = DataTransformation() 
    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTrainer() 
    model_trainer.initiate_model_trainer(train_arr, test_arr)










#     import os
# import sys
# import logging
# import pandas as pd
# import requests
# import sqlite3  # as example for SQL
# from dataclasses import dataclass
# from sklearn.model_selection import train_test_split

# # Example Custom Exception
# class CustomException(Exception):
#     def __init__(self, message, error_detail: sys):
#         super().__init__(message)
#         _, _, exc_tb = error_detail.exc_info()
#         self.lineno = exc_tb.tb_lineno if exc_tb else None
#         self.filename = exc_tb.tb_frame.f_code.co_filename if exc_tb else None

#     def __str__(self):
#         return f"{self.args[0]} (File: {self.filename}, Line: {self.lineno})"


# # CONFIG
# @dataclass
# class DataIngestionConfig:
#     source_type: str = "csv"   # csv | excel | sql | api
    # source_path: str = r"data\stud.csv"  # or query / url
    # raw_data_path: str = os.path.join("artifacts", "data.csv")
    # train_data_path: str = os.path.join("artifacts", "train.csv")
    # test_data_path: str = os.path.join("artifacts", "test.csv")


# # INGESTION CLASS
# class DataIngestion:
#     def __init__(self, config: DataIngestionConfig = DataIngestionConfig()):
#         self.ingestion_config = config

#     def _load_data(self):
#         """Load data from different sources depending on config."""
#         stype = self.ingestion_config.source_type.lower()

#         if stype == "csv":
#             return pd.read_csv(self.ingestion_config.source_path)

#         elif stype == "excel":
#             return pd.read_excel(self.ingestion_config.source_path)

#         elif stype == "sql":
#             # Example: SQLite (you can adjust for MySQL, Postgres, etc.)
#             conn = sqlite3.connect("my_database.db")
#             return pd.read_sql(self.ingestion_config.source_path, conn)

#         elif stype == "api":
#             response = requests.get(self.ingestion_config.source_path)
#             response.raise_for_status()
#             return pd.DataFrame(response.json())

#         else:
#             raise ValueError(f"Unsupported source type: {stype}")

#     def initiate_data_ingestion(self):
#         logging.info("Entered the data ingestion method")

#         try:
#             df = self._load_data()

#             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

#             df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

#             logging.info("Train-test split initialized")
#             train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

#             train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
#             test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

#             logging.info("Splitting Done.")

#             return (
#                 self.ingestion_config.train_data_path,
#                 self.ingestion_config.test_data_path
#             )

#         except Exception as e:
#             raise CustomException(e, sys)
