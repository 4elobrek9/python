from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
pipe = Pipeline([("scaler", StandardScaler()), ("svc", SVC())])
pipe.fit([[1, 2], [3, 4]], [0, 1])
print("Prediction:", pipe.predict([[5, 6]]))