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
                # "Linear Regression": LinearRegression(),
                "K-Neighbors Classifier": KNeighborsRegressor(),
                "AdaBoost Classifier": AdaBoostRegressor(),
            }

            params = {
                "Random Forest": {
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Decision Tree": {
                    'criterion': ['squared_error', 'friedman_mse', 'absolute_error', 'poisson']
                },
                "Gradient Boosting": {
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    'n_estimators':[8,16,32,64,128,256]
                },
                # "Linear Regression": {
                #     # optional
                #     'fit_intercept': [True, False]
                # },
                "K-Neighbors Classifier": {
                    'n_neighbors': [3,5,7,9,11]
                },
                "AdaBoost Regressor": {
                    'learning_rate':[.1,.01,0.5,.001],
                    'n_estimators': [8,16,32,64,128,256],
                    # 'loss': ['linear','square','exponential']
                }
            }


            model_report:dict = evaluate_model(X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test, models=models, params=params)
            print("model_report", model_report )
            # get best model 
            best_model_name = max(model_report, key = lambda x: model_report[x]["score"])
            best_model_info = model_report[best_model_name]

            best_model = best_model_info["model"]
            best_model_score = best_model_info["score"]
            best_params = best_model_info["params"]

            save_object(
                file_path=self.model_trainer_config.trianed_model_file,
                obj=best_model
            )

            predicted = best_model.predict(X_test)
            r2_score_ = r2_score(y_test, predicted)
            logging.info(f"Best model found : {best_model_name} with r2 score: {r2_score_} and parameters: {best_params}")
            return r2_score_


        except Exception as e: 
            EC = CustomException(e,sys)
            logging.error(EC)
            raise EC
