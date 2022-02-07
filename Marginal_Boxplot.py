import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Dataset/mpg_ggplot2.csv")

# CREATE FIG AND GRIDSPEC
fig = plt.figure(figsize=(16,10),dpi = 80)
grid = plt.GridSpec(4,4,wspace=0.2,hspace=0.5)

# DEFINE AXES OF PLOTS ---- scatter plot --- main ----histogram- right and bottom axis
ax_main = fig.add_subplot(grid[:-1,:-1])
ax_right = fig.add_subplot(grid[:-1,-1],xticklabels=[],yticklabels=[])
ax_bottom = fig.add_subplot(grid[-1,0:-1],xticklabels=[],yticklabels=[])

# SCATTER PLOT ON MAIN AXES
ax_main.scatter('displ','hwy',data=df,s=df.cty*4,c = df.manufacturer.astype('category').cat.codes,cmap='tab10',alpha=0.9,linewidth=0.6,edgecolors='black')

# BOX PLOT ON RIGHT AXES
sns.boxplot(y = df.hwy, ax=ax_right, orient="v")
sns.boxplot(x = df.displ, ax=ax_bottom, orient="h")

ax_bottom.set(xlabel=" ")
ax_right.set(ylabel=" ")

ax_main.set(title='Scatterplot with Boxplots \n displ vs hwy',xlabel='displ',ylabel='hwy')
ax_main.title.set_fontsize(20)

for item in ([ax_main.xaxis.label,ax_main.yaxis.label]+ax_main.get_xticklabels()+ax_main.get_yticklabels()):
    item.set_fontsize(14)


xlabels = ax_main.get_xticks().tolist()
ax_main.set_xticklabels(xlabels)
plt.show()