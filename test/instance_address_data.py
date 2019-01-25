import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import random
out=open('instance_used_requested.csv','r')
meta_file=csv.reader(out)
index=0
x=np.arange(0.0,8.0,0.04)
max_cpu=[]
avg_cpu=[]
min_cpu=[]
max_mem=[]
avg_mem=[]
min_mem=[]
for mac in meta_file :
    if  index ==1 :
        max_cpu=mac
    if index ==2:
        avg_cpu=mac
    if index ==3:
        min_cpu=mac
    if index ==4:
        max_mem=mac
    if index ==5:
        avg_mem=mac
    if index ==6 :
        min_mem=mac
    index +=1
m=0
while m<200:
    max_cpu[m]=float(max_cpu[m])
    avg_cpu[m] = float(avg_cpu[m])
    min_cpu[m] = float(min_cpu[m])
    max_mem[m] = float(max_mem[m])
    avg_mem[m] = float(avg_mem[m])
    min_mem[m] = float(min_mem[m])
    m=m+1

m=0
while m<200 :
    if min_cpu[m]==1.0:
        min_cpu[m]=0
    if min_mem[m]==1.0:
        min_mem[m]=0
    if max_cpu[m]==0:
        max_cpu[m] = max_cpu[m - 1] + random.uniform(-0.02, 0.02)
    if max_mem[m]==0:
        max_mem[m] = max_mem[m - 1] + random.uniform(-0.02, 0.02)
    if avg_cpu[m] == 0:
        avg_cpu[m] = avg_cpu[m - 1] + random.uniform(-0.02, 0.02)
    if avg_mem[m] == 0:
        avg_mem[m] = avg_mem[m - 1] + random.uniform(-0.02, 0.02)
    m=m+1
print (x)
print (max_cpu)
plt.xlim(0,8)
plt.ylim(0,15.0)
plt.xticks(np.linspace(0,8,9,endpoint=True))
plt.yticks(np.linspace(0,15.0,11,endpoint=True))
plt.subplot(1,2,1)
plt.plot(x,max_cpu,color='red')
plt.plot(x,avg_cpu,color='blue')
plt.plot(x,min_cpu,color='green')
plt.subplot(1,2,2)
plt.plot(x,max_mem,color='red')
plt.plot(x,avg_mem,color='blue')
plt.plot(x,min_mem,color='green')
plt.savefig("instance_used_requested_2.jpg")
plt.show()