"""Write a function to generate N samples from a normal distribution
and plot the histogram"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

N = 10000


def norm_dist_hist(N, mean=0, std_dev=1):
    x = np.random.normal(loc=mean, scale=std_dev, size=N)
    sns.histplot(x, bins=20, kde=True)
    plt.title(f"Histogram of {N} Samples from N({mean}, {std_dev}^2)")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()


X = norm_dist_hist(N)
