from sklearn.decomposition import PCA
pca = PCA(n_components=1)
pca.fit([[1, 2], [3, 4]])
print("Transformed:", pca.transform([[5, 6]]))