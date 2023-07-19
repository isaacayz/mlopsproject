import os
import sys
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exceptions import CustomException
from src.logger import logging
from src.utils import evaluate_models, save_object


@dataclass
class ModelTrainerConfig:
    model_trainer_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_arr, test_arr):
        logging.info('Splits training and testing data input')
        try:
            X_train, y_train, X_test, y_test =(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            # declare models as a dictionary
            models = {
                'Random Forest': RandomForestRegressor(),
                'Decision Tree': DecisionTreeRegressor(),
                'Gradient Boosting': GradientBoostingRegressor(),
                'Linear Regression': LinearRegression(),
                'K-Neighbors Classifier': KNeighborsRegressor(),
                'XGBClassifier': XGBRegressor(),
                'CatBoosting Classifier': CatBoostRegressor(verbose=False),
                'AdaBoosting Classifier': AdaBoostClassifier()
            }

            model_report:dict = evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models)

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score) ]
            
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException('The models are performing badly')
            logging.info(f'We have a very good model which is {best_model_name}')

            save_object(
                file_path= self.model_trainer_config.model_trainer_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)

            r2_squared = r2_score(y_test, predicted)

            return r2_squared
        
        except Exception as e:
            raise CustomException(e, sys)