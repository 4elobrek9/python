import pandas as pd
import matplotlib.pyplot as plt
data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
df.plot(kind="bar")
plt.show()