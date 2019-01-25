import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

data_segment=[]
seg=0
while seg<200 :
    data_segment.append(0)
    seg=seg+1

data = pd.read_csv('F:\\download\\machine_usage\\machine_usage.csv', header=None,sep=None,error_bad_lines=False,engine = 'python',iterator=True)
loop = True
chunkSize = 1
index=0
num_y=np.zeros(200)
max_y=np.zeros(200)
avg_y=np.zeros(200)
min_y=np.zeros(200)
m=0
while m<200 :
    min_y[m]=100
    m=m+1
x=np.arange(0.0,8.0,0.04)
print (data)
machine_meta_file=csv.reader(open('D:\\batch_instance\\batch_instance.csv','r'))
for mac in machine_meta_file :
    print (mac)
    index=index+1
    if index>=100:
        break

