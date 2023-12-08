from pickle import dump, load
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import RobustScaler

model = load(open("randomforest.pkl", "rb"))
scaler = load(open("robust_scaler.pkl", "rb"))


def get_scale_data(data):
    return scaler.transform(data)


def get_prediction(data):
    scaled_data = get_scale_data(data)
    return model.predict(scaled_data)
