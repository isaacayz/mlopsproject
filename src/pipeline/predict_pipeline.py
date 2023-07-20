import sys
import pandas as pd
from src.exceptions import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self) -> None:
        pass


class CustomData:
    def __init__(self,
                gender : str,
                race_ethnicity: str,
                parental_level_of_education,
                lunch : str,
                test_preparation_score: str,
                reading_score: str,
                writing_score: str
                 ):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_score = test_preparation_score
        self.reading_score = reading_score
        self.writing_score = writing_score