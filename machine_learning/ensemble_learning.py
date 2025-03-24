from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit([[1, 2], [3, 4]], [0, 1])
print("Prediction:", model.predict([[5, 6]]))