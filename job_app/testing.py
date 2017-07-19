import os
import logging
import pandas as pd

from pipeline import full_pipeline
from utils import get_testing_data, save_dataframe, get_saved_model
from settings import TESTING__DATA_PATH, SAVE_PREDICTION_PATH, SAVE_MODEL_PATH


def test_model():
    """
    Test the job application model and save the predictions
    :return: 
    """
    jobs_test = get_testing_data(TESTING__DATA_PATH)
    logging.info("Transforming data")
    jobs_test_prepared = full_pipeline.fit_transform(jobs_test)
    logging.info("Loading the model data")
    model = get_saved_model(SAVE_MODEL_PATH)
    app_test_predictions = model.predict(jobs_test_prepared)
    job_id_test = jobs_test["job_id"]
    pred_test = pd.DataFrame(data={"job_id":job_id_test, "prediction": app_test_predictions})
    logging.info("Saving new predictions")
    save_dataframe(pred_test, SAVE_PREDICTION_PATH, columns=["job_id", "prediction"])


if __name__ == "__main__":
    dir_path = os.path.abspath(os.path.dirname(__file__))
    abs_path = os.path.join(dir_path, '../job_app.log')
    logging.basicConfig(filename=abs_path, level=logging.DEBUG, format='%(asctime)s %(message)s')
    test_model()