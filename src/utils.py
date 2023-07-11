import os, sys
import pandas as pd
import numpy as np
from src.exceptions import CustomException
import dill

def save_object(file_path, obj):
    try:
        dir_name = os.path.join(file_path)

        os.makedirs(dir_name, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e, sys)