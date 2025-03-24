from sklearn.metrics import accuracy_score
y_true = [0, 1, 1, 0]
y_pred = [0, 1, 0, 0]
print("Accuracy:", accuracy_score(y_true, y_pred))