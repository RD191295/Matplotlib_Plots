import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


df = pd.read_csv("Dataset/mpg_ggplot2.csv")

df_select = df.loc[df.cyl.isin([4, 8]),:]

sns.set_style("whitegrid")
gridobj =  sns.lmplot(x= "displ", y="hwy", data=df_select, hue="cyl", height=4.5, aspect=1.6, robust=True, palette="tab10",
                      scatter_kws= dict(s = 60, linewidths = 0.7, edgecolors = "black"))

gridobj.set(xlim=(0.5, 7.5), ylim=(0, 50))
plt.title("Scatterplot with line of best fit grouped by no of cylinders",fontsize=16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

plt.show()