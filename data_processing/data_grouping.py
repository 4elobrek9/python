from itertools import groupby
data = [("a", 1), ("a", 2), ("b", 3)]
grouped = {k: list(v) for k, v in groupby(data, lambda x: x[0])}
print("Grouped:", grouped)