from sklearn.feature_selection import SelectKBest, f_classif
X = [[1, 2], [3, 4], [5, 6]]
y = [0, 1, 0]
selector = SelectKBest(f_classif, k=1)
selector.fit(X, y)
print("Selected Features:", selector.get_support())