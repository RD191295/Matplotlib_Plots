import  matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

df = pd.read_csv("Dataset/mtcars.csv")

#print(df.head())

plt.figure(figsize=(16,10),dpi = 80)

sns.heatmap(df.corr(),annot=True,cmap="RdYlGn",xticklabels=df.corr().columns,yticklabels=df.corr().columns)

# TITLE AND LABELS
plt.title("Correlogram of mtcars",fontsize=22)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.show()