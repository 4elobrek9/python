from sklearn.preprocessing import StandardScaler
import numpy as np
data = np.array([[1, 2], [3, 4], [5, 6]]
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
print("Scaled Data:", scaled_data)