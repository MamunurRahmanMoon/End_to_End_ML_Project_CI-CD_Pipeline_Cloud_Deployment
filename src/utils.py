import os
import sys
import dill
import numpy as np
import pandas as pd
from src.exception import CustomException


def save_object(file_path, obj):
    """
    Save an object to a file using pickle.
    """
    try:
        # Path to the directory where the file will be saved
        dir_path = os.path.dirname(file_path)

        # Create the directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)
        
        # Save the object to the specified file path using dill
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys) from e