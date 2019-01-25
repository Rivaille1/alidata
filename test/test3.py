import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
"""
index =0
task_meta_file=csv.reader(open('D:\\batch_instance\\batch_instance.csv','r'))
for mac in task_meta_file :
    print (mac)
    print (mac[2]+mac[1])


    index=index+1
    if index>=100 :break
"""
plt.xlim(0,8)
plt.ylim(0,1.0)
plt.xticks(np.linspace(0,8,9,endpoint=True))
plt.yticks(np.linspace(0,1.0,11,endpoint=True))
plt.show()

