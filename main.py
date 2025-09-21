import os  
import sys 
from src.exception import CustomException
from src.logger import logging 
import pandas as pd 
from dataclasses import dataclass 
from sklearn.model_selection import train_test_split 

from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    obj = DataIngestion() 
    train_data , test_data = obj.initiate_data_ingestion() 

    data_transformation = DataTransformation() 
    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTrainer() 
    model_trainer.initiate_model_trainer(train_arr, test_arr)