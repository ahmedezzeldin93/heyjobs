import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):

    def __init__(self, salary_ix, hours_ix):
        self.salary_ix = salary_ix
        self.hours_ix = hours_ix

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        salary_per_hour = X[:, self.salary_ix] / X[:, self.hours_ix]
        return np.c_[X, salary_per_hour]


class DataFrameSelector(BaseEstimator, TransformerMixin):

    def __init__(self, attribute_names):
        self.attribute_names = attribute_names

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.attribute_names].values


class NumpySelector(BaseEstimator, TransformerMixin):

    def __init__(self, indx):
        self.indx = indx

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[:, self.indx]
