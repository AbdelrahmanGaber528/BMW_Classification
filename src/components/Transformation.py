import pandas as pd 
import numpy as np
import sys
import joblib
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from utils.common import create_directories
from src import customException
from src.entity.config_entity import DataTransformationConfig 
from src.logger import get_logger

logging = get_logger()

class DataTransformation:

    def __init__(self, data_transformation_config: DataTransformationConfig):
        self.data_transformation = data_transformation_config
    
    def train_test_spliting(self):
        """Split dataset into train and test and save to CSVs."""
        try:
            data = pd.read_csv(self.data_transformation.data_path)

            train, test = train_test_split(data, test_size=0.2, random_state=42)


            # Create root directory if it doesn't exist
            create_directories([self.data_transformation.root_dir])
            logging.info(f"Created directory at {self.data_transformation.root_dir}")
            
            train.to_csv(self.data_transformation.train_path, index=False)
            test.to_csv(self.data_transformation.test_path, index=False)

            logging.info(
                f"Splitted data into train ({train.shape}) and test ({test.shape}) sets"
            )
        except Exception as e:
            raise customException(e, sys)



    def get_data_transformer_object(self, df: pd.DataFrame):
        """Create column transformer object for preprocessing."""
        try:

            X = df.drop(columns=["Sales_Classification"], axis=1)

            numerical_columns = X.select_dtypes(include=np.number).columns.tolist()
            categorical_columns = X.select_dtypes(include=["object", "category"]).columns.tolist()

            numerical_transformer = StandardScaler()
            categorical_transformer = OneHotEncoder(handle_unknown="ignore")

            preprocessor = ColumnTransformer(
                transformers=[
                    ("num", numerical_transformer, numerical_columns),
                    ("cat", categorical_transformer, categorical_columns)
                ]
            )

            logging.info("Column transformer object created successfully")

            return preprocessor

        except Exception as e:
            raise customException(e, sys)
        



    def initiate_data_transformation(self):
        """Run the whole transformation pipeline: split, preprocess, encode target."""
        try:
            # Step 1: Split train/test and save
            self.train_test_spliting()

            # Step 2: Read train/test back
            train = pd.read_csv(self.data_transformation.train_path)
            test = pd.read_csv(self.data_transformation.test_path)

            # Step 3: Build preprocessor
            preprocessor = self.get_data_transformer_object(train)

            target_column_name = "Sales_Classification"

            input_feature_train_df = train.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train[target_column_name]

            input_feature_test_df = test.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test[target_column_name]

            logging.info("Splitting input and target features Success.")

            # Step 4: Fit/transform features
            logging.info("Applying preprocessing object on training and testing datasets.")

            X_train = preprocessor.fit_transform(input_feature_train_df)
            X_test = preprocessor.transform(input_feature_test_df)

            # Step 5: Encode target column
            y_train = target_feature_train_df.replace({"Low": 0, "High": 1})
            y_test = target_feature_test_df.replace({"Low": 0, "High": 1})

            # Step 6: Save preprocessor (after fitting)
            joblib.dump(preprocessor, self.data_transformation.preprocessor_object_file)

            logging.info(
                f"Preprocessor object saved at {self.data_transformation.preprocessor_object_file}"
            )

            logging.info("Data transformation completed successfully.")

            return (
                X_train,
                X_test,
                y_train,
                y_test
            )

        except Exception as e:
            raise customException(e, sys)
