import os
import sys
import joblib
from dataclasses import dataclass
from typing import Dict, List, Tuple
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object




@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')

@dataclass
class DataTransformation:
    data_transformation_config: DataTransformationConfig = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns = ['writing_score', 'reading_score']
            categorical_columns = [
                'gender', 
                'race_ethnicity', 
                'parental_level_of_education', 
                'lunch', 
                'test_preparation_course']
            
            numerical_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
                
                ])
            
            categorical_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('onehotencoder', OneHotEncoder(handle_unknown='ignore')),
                ('scaler', StandardScaler(with_mean=False))
                
                ])
            
            logging.info(f"Pipeline object created for numerical and categorical columns")

            preprocessor = ColumnTransformer(
                transformers=[
                    ('numerical_pipeline', numerical_pipeline, numerical_columns),
                    ('categorical_pipeline', categorical_pipeline, categorical_columns)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
            logging.info("Error occurred during data")


        
    def initiate_data_transformation(self, train_path, test_path) :


        try:
            logging.info("Data Transformation started")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")


            logging.info("Obtaining preprocessing object")
            preprocessing_obj = self.get_data_transformer_object()

            # Defining target and input features
            target_column_name = 'math_score'
            numerical_columns = ['writing_score', 'reading_score']

            # Creating dataframe for Training input features and target feature
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            # Creating dataframe for Testing input features and target feature
            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]    
            
            # Applying preprocessing object on training and testing dataframes
            logging.info("Applying preprocessing object on training and testing dataframes")
            
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
    
            # 
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            # Saving the preprocessor object
            logging.info("Saving preprocessing object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e, sys)
            logging.info("Error occurred during data transformation")