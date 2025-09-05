from sklearn.metrics import f1_score, confusion_matrix, accuracy_score, recall_score, classification_report, precision_score
from sklearn.model_selection import RandomizedSearchCV
import sys
from src import customException

def evaluate_model(models, params, x_train,  x_test, y_train,  y_test):

    model_list = []
    evaluate_report = {}

    for model, object_of_model in models.items():
        try:
            if model in params and params[model]:
                RandomizedSearch = RandomizedSearchCV(
                    estimator=object_of_model,
                    param_distributions=params[model],
                    n_iter=10,
                    cv=3,
                    verbose=2,
                    random_state=42,
                    n_jobs=-1
                )
                RandomizedSearch.fit(x_train, y_train)
                best_model = RandomizedSearch.best_estimator_
            else:
                best_model = object_of_model
                best_model.fit(x_train, y_train)

            y_pred = best_model.predict(x_test)

            accuracy = accuracy_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred, average='weighted')
            recall = recall_score(y_test, y_pred, average='weighted')
            precision = precision_score(y_test, y_pred, average='weighted')
            cm = confusion_matrix(y_test, y_pred)
            report_classification = classification_report(y_test, y_pred)

            model_list.append({
                'model_name': model,
                'best_model': best_model,
                'accuracy': accuracy,
                'f1': f1,
                'recall': recall,
                'precision': precision,
                'cm': cm,
                'report_classification': report_classification
            })
            evaluate_report[model] = [accuracy, f1, recall, precision, cm, report_classification]

        except Exception as e:
            raise customException(e, sys)

    best_model = max(model_list, key=lambda x: x['f1'])

    return best_model, model_list, evaluate_report