import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object, evaluate_models


class ModelTrainerConfig:
    def __init__(self):
        self.trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, val_array, test_array):
        try:
            logging.info(
                "Splitting input and target features for training, validation, and testing"
            )

            # Split arrays into input and target features
            X_train, y_train = train_array[:, :-1], train_array[:, -1]
            X_val, y_val = val_array[:, :-1], val_array[:, -1]
            X_test, y_test = test_array[:, :-1], test_array[:, -1]

            # Define models
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbors Classifier": KNeighborsRegressor(),
                "XGBClassifier": XGBRegressor(),
                "CatBoosting Classifier": CatBoostRegressor(verbose=False),
                "AdaBoost Classifier": AdaBoostRegressor(),
            }

            # Evaluate models on training and validation sets
            model_report = evaluate_models(
                X_train=X_train,
                y_train=y_train,
                X_test=X_val,
                y_test=y_val,
                models=models,
            )

            # Get the best model score and name
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            # Check if the best model meets the threshold
            if best_model_score < 0.7:
                raise CustomException("No best model found with acceptable performance")

            logging.info(
                f"Best model selected: {best_model_name} with validation R² score: {best_model_score}"
            )

            # Save the best model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model,
            )

            # Test the best model on the test set
            logging.info("Testing the best model on the test set")
            predicted = best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)

            logging.info(f"Test R² score for the best model: {r2_square}")
            return (
                best_model_name,
                r2_square,
            )  # Return the best model name and test R² score

        except Exception as e:
            logging.error("Exception occurred in model trainer")
            raise CustomException(e, sys)
