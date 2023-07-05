import os
import sys
import pandas as pd
from src.exceptions import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


class DataIngestionConfig:
    pass