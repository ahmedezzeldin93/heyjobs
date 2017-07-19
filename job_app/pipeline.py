from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import FeatureUnion
from sklearn_pandas import DataFrameMapper
from sklearn.preprocessing import LabelBinarizer

from transformers import DataFrameSelector, CombinedAttributesAdder, NumpySelector
from utils import get_training_data


jobs = get_training_data()

jobs_num = jobs.drop(["job_id", "job_type", "city"], axis=1)
jobs_cat = jobs.drop(["job_id","salary"], axis=1)

num_attribs_hour = ["salary", "hours"]
num_attribs_all = ["salary", "salary_per_hour"]

num_pipeline = Pipeline([
        ('selector_1', DataFrameSelector(num_attribs_hour)),
        ('attribs_adder', CombinedAttributesAdder(0,1)),
        ('selector_2', NumpySelector([0,2])),
        ('std_scaler', StandardScaler()),
])

mapper = DataFrameMapper(
    [(cat, LabelBinarizer()) for cat in jobs_cat]
)

cat_pipeline = Pipeline([
        ('label_multibinarizer', mapper)
])

full_pipeline = FeatureUnion(transformer_list=[
        ("num_pipeline", num_pipeline),
        ("cat_pipeline", cat_pipeline),
])
