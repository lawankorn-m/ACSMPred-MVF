import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.base import BaseEstimator, ClassifierMixin
class PLS(BaseEstimator, ClassifierMixin):
    def __init__(self, iter=500):
        self.iter = iter
        self.clf = PLSRegression(n_components=2, max_iter=self.iter)
    def fit(self, X, y):
        self.classes_ = np.unique(y)
        self.clf.fit(X,y)
        return self
    def predict(self, X):
        pr = [np.round(min(max(item[0],0.000001),0.999999)) for item in self.clf.predict(X)]
        return np.array(pr)
    def predict_proba(self, X):
        p_all = []
        p_all.append([1-min(max(item[0],0.000001),0.99999) for item in self.clf.predict(X)])
        p_all.append([min(max(item[0],0.000001),0.99999) for item in self.clf.predict(X)])
        return np.transpose(np.array(p_all))
