import os
from src import get_logger
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from typeguard import typechecked
from box import ConfigBox 
from pathlib import Path
from typing import Any

logger = get_logger()

@typechecked
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns ConfigBox

    Args:
        path_to_yaml (Path): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: config data as attributes
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)   # <-- FIXED here
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    


@typechecked
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories"""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@typechecked
def save_json(path: Path, data: dict):
    """save json data"""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")


@typechecked
def load_json(path: Path) -> ConfigBox:   # <-- FIXED here
    """load json files data"""
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)   # <-- FIXED here


@typechecked
def save_bin(data: Any, path: Path):
    """save binary file"""
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@typechecked
def load_bin(path: Path) -> Any:
    """load binary data"""
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@typechecked
def get_size(path: Path) -> str:
    """get size in KB"""
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
