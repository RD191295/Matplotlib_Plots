import matplotlib.pyplot as plt
from matplotlib import patches
from scipy.spatial import ConvexHull
import warnings
import numpy as np
import pandas as pd
import seaborn as sns

warnings.simplefilter('ignore')

# LOAD DATA
midwest = pd.read_csv("Dataset\midwest_filter.csv")
categories = np.unique(midwest['category'])
colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]


# DRAW SCATTER PLOT FOR DIFFERENT CATEGORIES
fig = plt.figure(figsize=(16,10), dpi=80,facecolor='w', edgecolor='k')
for i,category in enumerate(categories):
    plt.scatter("area","poptotal",data = midwest.loc[midwest['category'] == category,:],s="dot_size",color=colors[i],edgecolors = "black",linewidths=0.5,label=str(category))

# Step 3: Encircling
# https://stackoverflow.com/questions/44575681/how-do-i-encircle-different-data-sets-in-scatter-plot
def encircle(x,y,ax=None,**kw):
    if not ax:
        ax = plt.gca()

    p = np.c_[x,y]
    hull = ConvexHull(p)
    poly = plt.Polygon(p[hull.vertices,:],**kw)
    ax.add_patch(poly)

midwest_encircle_data =  midwest.loc[midwest.state == "IN"]


# DRAW POLYGON SURROUNDING THE VERTICES
encircle(midwest_encircle_data.area,midwest_encircle_data.poptotal,alpha=0.1,ec="k",fc="gold")
encircle(midwest_encircle_data.area,midwest_encircle_data.poptotal,linewidth=1.5,ec="firebrick",fc="none")

plt.gca().set(xlim=(0.0,0.1),ylim=(0.0,90000.0),xlabel="Area",ylabel="Population")
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.title("Bubble Plot with encircling",fontsize=20)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

plt.show()