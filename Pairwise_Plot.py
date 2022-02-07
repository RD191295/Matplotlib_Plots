import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("Dataset\iris.csv")
plt.figure(figsize=(16, 10),dpi=80)
sns.pairplot(df,kind= "scatter", hue="Species", plot_kws={"s": 80, "edgecolor": "white","linewidth":2.5})
sns.pairplot(df,kind= "reg", hue="Species")
plt.show()