import os
import urllib.request as request
import zipfile
from mlProject import logger
from mlProject.utils.common import get_size
from pathlib import Path
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import (DataTransformationConfig)


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        data.drop('type',axis=1, inplace = True)
        data['fixed acidity'].fillna(data['fixed acidity'].mean(), inplace=True)
        data['volatile acidity'].fillna(data['volatile acidity'].mean(), inplace=True)
        data['citric acid'].fillna(data['citric acid'].mean(), inplace=True)
        data['residual sugar'].fillna(data['residual sugar'].mean(), inplace=True)
        data['chlorides'].fillna(data['chlorides'].mean(), inplace=True)
        data['pH'].fillna(data['pH'].mean(), inplace=True)
        data['sulphates'].fillna(data['sulphates'].mean(), inplace=True)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)