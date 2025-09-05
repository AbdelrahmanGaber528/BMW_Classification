import sys
from src.logger import get_logger
from src import customException
from src.config.configuration import ConfigurationManager
from src.components.Ingestion import DataIngestion
from src.components.Transformation import DataTransformation
from src.components.trainer import ModelTrainer

logging = get_logger()

def main():
    try:
        logging.info(">>>> Starting BMW Classification Pipeline <<<<")

        # 1. Configuration
        config = ConfigurationManager()

        # 2. Data Ingestion
        logging.info(">>>>> Stage 1: Data Ingestion Started <<<<<")
        data_ingestion_config = config.get_data_ingestion_config()
        ingestion = DataIngestion(config=data_ingestion_config)
        ingestion.initiate_data_ingestion()
        logging.info(">>>>> Stage 1: Data Ingestion Completed <<<<<")

        # 3. Data Transformation
        logging.info(">>>>> Stage 2: Data Transformation Started <<<<<")
        data_transformation_config = config.get_data_transformation_config()
        transformation = DataTransformation(config=data_transformation_config)
        X_train, X_test, y_train, y_test = transformation.initiate_data_transformation()
        logging.info(">>>>> Stage 2: Data Transformation Completed <<<<<")

        # 4. Model Training
        logging.info(">>>>> Stage 3: Model Training Started <<<<<")
        model_trainer_config = config.get_model_trainer_config()
        trainer = ModelTrainer(config=model_trainer_config)
        trainer.train(X_train,  X_test, y_train, y_test)
        logging.info(">>>>> Stage 3: Model Training Completed <<<<<")

        logging.info(">>>> BMW Classification Pipeline Finished Successfully <<<<")

    except Exception as e:
        logging.error("Pipeline failed")
        raise customException(e, sys)


if __name__ == "__main__":
    main()
