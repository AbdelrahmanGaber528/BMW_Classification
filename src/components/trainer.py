import sys
import joblib
from sklearn.linear_model import LogisticRegression , SVC  , AdaBoostClassifier , KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from src.components.Evaluate import evaluate_model
from src import customException
from src.entity.config_entity import ModelTrainerConfig 
from src.logger import get_logger

logging = get_logger()


class ModelTrainer:

    def __init__ (self, model_trainer_config : ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def train(self, X_train, y_train , X_test , y_test):

        try:

            models = {
                "LogisticRegression": LogisticRegression(),
                "DecisionTreeClassifier": DecisionTreeClassifier(),
                "SVC": SVC(),
                "RandomForestClassifier": RandomForestClassifier(),
                "AdaBoostClassifier": AdaBoostClassifier(),
                "KNeighborsClassifier": KNeighborsClassifier(),
                "XGBClassifier": XGBClassifier(),
                "CatBoostClassifier": CatBoostClassifier()
            }

            params = self.model_trainer_config.params
            
            best_model, model_list, evaluate_report = evaluate_model(
                models, params, X_train, y_train, X_test, y_test
            )
            
            logging.info(f"Best model: {best_model['model_name']} with F1 score: {best_model['f1']}")
            
            
            joblib.dump(best_model['best_model'], self.model_trainer_config.model_path)
            logging.info(f"Best model saved at {self.model_trainer_config.model_path}")
            return best_model, model_list, evaluate_report
        
        except Exception as e:
            raise customException(e, sys)