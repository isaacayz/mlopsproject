from data_ingestion import DataIngestion
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
from src.exceptions import CustomException
from src.logger import logging
import sys, os


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self) -> None:
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_obj(self):
        try:
            num_features = ['reading_score', 'writing_score']
            cat_features = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder', OneHotEncoder()),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )
            logging.info('Categorical columns standard scaling completed')
            logging.info('Numerical columns encoding completed')

            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, num_features),
                    ('cat_pipeline', cat_pipeline, cat_features)
                ]
            )

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
        except:
            pass