from pathlib import Path
from src.entity.config_entity import ModelTrainerConfig

CONFIG_FILE_PATH = Path("config/config.yaml")
MODEL_PATH = Path("artifacts/model_trainer/bmw_model.pkl")
PREPROCESSOR_PATH = Path("artifacts/data_transformation/preprocessor.pkl")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")