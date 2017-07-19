import os
import pandas as pd
from sklearn.externals import joblib

from settings import SAVE_MODEL_PATH, SAVE_PREDICTION_PATH, TESTING__DATA_PATH, TRAINING__DATA_PATH


def read_dataframe(path, type='csv'):
    dir_path = os.path.abspath(os.path.dirname(__file__))
    abs_path = os.path.join(dir_path, path)
    if type == 'csv':
        df = pd.read_csv(abs_path)
    else:
        raise RuntimeError("file types other than csv is not supported")
    return df


def save_dataframe(dataframe, path=SAVE_PREDICTION_PATH, columns=[]):
    dir_path = os.path.abspath(os.path.dirname(__file__))
    abs_path = os.path.join(dir_path, path)
    dataframe.to_csv(abs_path, columns=columns, index=False)


def get_training_data(path=TRAINING__DATA_PATH):
    training_df = read_dataframe(path, "csv")
    jobs_variables = training_df.drop("applications", axis=1)
    return jobs_variables


def get_testing_data(path=TESTING__DATA_PATH):
    testing_df = read_dataframe(path, "csv")
    return testing_df


def get_training_labels(label, path=TRAINING__DATA_PATH):
    training_df = read_dataframe(path, "csv")
    jobs_labels = training_df[label].copy()
    return jobs_labels


def save_trained_model(model, path=SAVE_MODEL_PATH):
    dir_path = os.path.abspath(os.path.dirname(__file__))
    abs_path = os.path.join(dir_path, path)
    joblib.dump(model, abs_path)


def get_saved_model(path=SAVE_MODEL_PATH):
    dir_path = os.path.abspath(os.path.dirname(__file__))
    abs_path = os.path.join(dir_path, path)
    model = joblib.load(abs_path)
    return model
