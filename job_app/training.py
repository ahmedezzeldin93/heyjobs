import os
import logging
from sklearn.linear_model import LinearRegression

from pipeline import full_pipeline
from utils import get_training_data, get_training_labels, save_trained_model
from settings import TRAINING__DATA_PATH


def train_model():
    """
    Train the job application model and save the model
    :return: 
    """
    jobs_training = get_training_data(TRAINING__DATA_PATH)
    jobs_labels = get_training_labels("applications")
    logging.info("Transforming data")
    jobs_prepared = full_pipeline.fit_transform(jobs_training)
    logging.info("Training the model")
    lin_reg = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    lin_reg.fit(jobs_prepared, jobs_labels)
    logging.info("Saving the model")
    save_trained_model(lin_reg)


if __name__ == "__main__":
    dir_path = os.path.abspath(os.path.dirname(__file__))
    abs_path = os.path.join(dir_path, '../job_app.log')
    logging.basicConfig(filename=abs_path, level=logging.DEBUG, format='%(asctime)s %(message)s')
    train_model()
