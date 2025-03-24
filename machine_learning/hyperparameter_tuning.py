from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
param_grid = {"C": [0.1, 1, 10], "kernel": ["linear", "rbf"]}
grid_search = GridSearchCV(SVC(), param_grid)
grid_search.fit([[1, 2], [3, 4]], [0, 1])
print("Best Parameters:", grid_search.best_params_)