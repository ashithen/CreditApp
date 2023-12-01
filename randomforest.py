from pickle import dump, load
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

model = load(open("randomforest.pkl", "rb"))

def get_prediction(data):
    return model.predict(data)