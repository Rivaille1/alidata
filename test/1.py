import numpy as np
import matplotlib.pyplot as plt



dataSets = [8.2,7.3,7.4]


temp = []

count=3
i=0

plotDataset = [[], []]
plotDataset[0]=[7.3,7.4,8.3]
plotDataset[1]=[1/3,1/3,1/3]
plt.plot(plotDataset[0], plotDataset[1], '-', linewidth=2)

plt.show()
