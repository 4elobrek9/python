from sklearn.neighbors import KNeighborsClassifier
X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)
print("Prediction for 1.5:", model.predict([[1.5]]))