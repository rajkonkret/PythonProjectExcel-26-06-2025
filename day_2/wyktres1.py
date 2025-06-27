import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [4, 5, 6, 7]})
print(df)
#    A  B
# 0  1  4
# 1  2  5
# 2  3  6
# 3  4  7
print(df.describe())

df.plot.box()
plt.show()
