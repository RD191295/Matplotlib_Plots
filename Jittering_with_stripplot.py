import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("Dataset/mpg_ggplot2.csv")


fig,ax = plt.subplots(figsize=(16,12),dpi=80)

sns.stripplot(df.cty,df.hwy,jitter=0.25,linewidth=0.5,ax=ax,size = 8)

plt.title("Jitter with Stripplot to avoid overlapping of points",fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.show()