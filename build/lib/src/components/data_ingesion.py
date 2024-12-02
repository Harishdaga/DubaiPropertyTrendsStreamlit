import sys
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd


from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts', 'train.csv')
    test_data_path = os.path.join('artifacts', 'test.csv')
    raw_data_path = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Doing Data Ingestions')
        try:
            df = pd.read_csv('notebook/data/dubai_data.csv')
            df = df.drop(['id', 'price_per_sqft', 'neighborhood'], axis=1)
            if df.isna().sum().sum() > 0:
                df = df.dropna()
            if df.duplicated().sum() > 0:
                df = df.drop_duplicates(keep='first')
            logging.info('Raw data csv file reading done')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            target_columns = ['price']
            df = df[[col for col in df.columns if col not in target_columns] + target_columns]
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('train test data spliting initiated')

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, header=True, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, header=True, index = False)

            logging.info('Ingestion of data completed')

            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == '__main__':
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)
    model_trainer = ModelTrainer()
    best_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
    print(best_score)