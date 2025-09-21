import os, sys

from dataclasses import dataclass 
from src.logger import logging 
from src.exception import CustomException 
from src.utils import save_object, evaluate_model 

# from catboost import CatBoostRegressor
# from xgboost import XGBRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor


@dataclass 
class ModelTrainerConfig:
    trianed_model_file = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig() 

    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info("split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:, -1]
            ) 
            logging.info(f"X_train: {X_train.shape}\nX_test: {X_test.shape}\ny_train: {y_train.shape}\ny_test: {y_test.shape}")
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbors Classifier": KNeighborsRegressor(),
                "AdaBoost Classifier": AdaBoostRegressor(),
            }

            model_report:dict = evaluate_model(X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test, models=models)

            # get best model 
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            save_object(
                file_path=self.model_trainer_config.trianed_model_file,
                obj=best_model
            )

            predicted = best_model.predict(X_test)
            r2_score_ = r2_score(y_test, predicted)
            logging.info(f"Best model found : {best_model_name} with r2 score: {r2_score_}")
            return r2_score_


        except Exception as e: 
            EC = CustomException(e,sys)
            logging.error(EC)
            raise EC
