import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import (
    AdaBoostRegressor,
    RandomForestRegressor,
    GradientBoostingRegressor
)
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info('Spliting training and testing data')
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1], train_array[:, -1],
                test_array[:, :-1], test_array[:, -1]
            )
        
            models = {
                        'LinearRegression':LinearRegression(), 
                        'AdaBoostRegressor':AdaBoostRegressor(), 
                        'RandomForestRegressor':RandomForestRegressor(), 
                        'Ridge':Ridge(), 
                        'Lasso':Lasso(), 
                        'GradientBoostingRegressor':GradientBoostingRegressor()
                    }
            params = {
                        'LinearRegression':{
                            'fit_intercept':[True, False],
                        },
                        'AdaBoostRegressor':{
                            'n_estimators':[50, 100, 200],
                            'learning_rate':[0.1, 0.05, 0.01, 0.001],
                            'loss':['linear', 'square', 'exponential'],
                        },
                        'RandomForestRegressor':{
                            'n_estimators':[50, 100, 200],
                            'max_depth':[10, 20, 30],
                            'max_features':['sqrt', 'log2'],
                            'criterion':['absolute_error', 'friedman_mse'],
                        },
                        'Ridge':{
                            'alpha':[0.1, 1, 10, 100],
                            'fit_intercept':[True, False],
                        },
                        'Lasso':{
                            'alpha':[0.1, 1, 10, 100],
                        },
                        'GradientBoostingRegressor':{
                            'learning_rate':[0.1, 0.05, 0.01, 0.001],
                            'n_estimators':[50, 100, 200]
                        }
                    }
            model_report = evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models, params=params)
            
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]
            if best_model_score < 0.6:
                raise CustomException('No best model found')
            else:
                logging.info(f'best model found on testing dataset is {best_model_name}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)
            score = r2_score(y_test, predicted)
            return score






        except Exception as e:
            raise CustomException(e, sys)








