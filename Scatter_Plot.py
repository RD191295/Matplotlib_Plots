import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


plt.style.use('seaborn-whitegrid')
sns.set_style("white")

df = pd.read_csv("Dataset/midwest_filter.csv")

categories = np.unique(df['category'])
colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]

plt.figure(figsize=(16,10),dpi = 80, facecolor = 'w', edgecolor = 'k')

for i,category in enumerate(categories):
    plt.scatter('area','poptotal',data = df.loc[df.category == category,:],s = 20 , c = colors[i], label = category)


plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.legend(fontsize = 12)
plt.gca().set(xlim=(0.0,0.1), ylim=(0,90000),xlabel = 'Area', ylabel = 'Population')
plt.title("Scatter Plot of midwest Area vs Population",fontsize = 22)

plt.show()