from pathlib import Path
from src.entity.config_entity import ModelTrainerConfig

CONFIG_FILE_PATH = Path("config/config.yaml")
MODEL_PATH = Path(ModelTrainerConfig.model_path)
PREPROCESSOR_PATH = Path(ModelTrainerConfig.preprocessor_object_file)
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")