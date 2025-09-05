import sys
import pandas as pd
import joblib
from src.logger import get_logger
from src import customException
from src.constants import MODEL_PATH, PREPROCESSOR_PATH
logging = get_logger()

class PredictPipeline:
    def __init__(self):
        try:
            self.model = joblib.load(MODEL_PATH)
            logging.info(f"Loaded trained model from {MODEL_PATH}")

            self.preprocessor = joblib.load(PREPROCESSOR_PATH)
            logging.info(f"Loaded preprocessor from {PREPROCESSOR_PATH}")

        except Exception as e:
            logging.error("Error loading model or preprocessor")
            raise customException(e, sys)

    def predict(self, data: pd.DataFrame) -> str:
        try:
            logging.info("Starting prediction pipeline")

            # Apply preprocessing
            transformed_data = self.preprocessor.transform(data)
            logging.info("Applied preprocessing to input data")

            # Run predictions
            prediction = self.model.predict(transformed_data)[0]
            logging.info("Generated predictions")

            predict = "Low" if prediction == 0 else "High"

            return predict
        
        except Exception as e:
            logging.error("Error during prediction")
            raise customException(e, sys)
