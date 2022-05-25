import pandas as pd
import numpy as np
a = [[1, 2], [3, 4], [5, 6]]
# df = pd.DataFrame(a, columns=["x", "y"])
df = np.array(a)
print(df)
print(df[:, 1])
print(type(df[:, 1]))