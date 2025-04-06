import os
import sys
from src.exception import CustomException
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    """
    Data Ingestion configuration class to define the paths and parameters for data ingestion.
    """
    raw_data_dir: str = os.path.join('artifacts')  # Directory for raw data
    raw_data_path: str = os.path.join(raw_data_dir, 'data.csv')  # Full path to the raw data file
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    val_data_path: str = os.path.join('artifacts', 'val.csv')  # Path for validation data
    test_data_path: str = os.path.join('artifacts', 'test.csv')


@dataclass
class DataIngestion:
    ingestion_config: DataIngestionConfig = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")
        try:
            # Read the dataset from a CSV file
            df = pd.read_csv("notebooks/data/stud.csv")
            logging.info("Read the dataset as dataframe")

            # Make directories for the output files if they do not exist
            os.makedirs(self.ingestion_config.raw_data_dir, exist_ok=True)

            # Save the raw data to a CSV file
            logging.info("Saving the raw data to CSV")
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Split the data into training and testing sets
            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info("Train-test split completed")

            # Further split the training set into training and validation sets
            logging.info("Train-validation split initiated")
            train_set, val_set = train_test_split(train_set, test_size=0.2, random_state=42)
            logging.info("Train-validation split completed")

            # Save the training, validation, and testing sets to CSV files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            val_set.to_csv(self.ingestion_config.val_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Train, validation, and test data saved to CSV files")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.val_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            logging.error("Error occurred during data ingestion")
            raise CustomException(e, sys) from e


if __name__ == "__main__":
    data_ingestion = DataIngestion()
    train_data, val_data, test_data = data_ingestion.initiate_data_ingestion()
    logging.info("Data Ingestion completed")

    data_transformation = DataTransformation()
    train_arr, val_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, val_data, test_data)
    logging.info("Data Transformation completed")

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, val_arr, test_arr))
    logging.info("Model Training completed")