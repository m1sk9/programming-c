import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "Hiragino Sans"

data = np.random.normal(50, 10, 1000)

plt.hist(data, bins=20, color='blue', alpha=0.7)
plt.title("Graph")
plt.show()
