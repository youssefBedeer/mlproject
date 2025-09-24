import os 
import sys
from src.exception import CustomException
import pandas as pd 
import numpy as np 
# import dill
import pickle
from sklearn.metrics import r2_score
from src.logger import logging
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys) 
    
def evaluate_model(X_train, X_test, y_train, y_test, models, params):
    try:
        report = {} # {model_name: score}

        for i in range(len(list(models))):
            model_name = list(models.keys())[i]
            model = list(models.values())[i]
            param = params[list(params.keys())[i]]

            # hyperparameter tunning
            gs = GridSearchCV(estimator=model, param_grid=param, cv=3)
            gs.fit(X_train, y_train)

            best_model = gs.best_estimator_

            best_model.fit(X_train,y_train)

            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            logging.info(f"best params for {model_name}: {gs.best_params_} with score: '{test_model_score}'")

            report[model_name] = {
                "score":test_model_score,
                "model": best_model,
                "params": gs.best_params_
                
            }

        return report


    except Exception as e: 
        EC = CustomException(e,sys)
        logging.error(EC)
        raise EC
    

