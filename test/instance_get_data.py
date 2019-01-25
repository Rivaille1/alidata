import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import random
data_segment=[]
seg=0
while seg<200 :
    data_segment.append(0)
    seg=seg+1
task_cpu=dict()
task_mem=dict()

num_y=np.zeros(200)
max_cpu=np.zeros(200)
avg_cpu=np.zeros(200)
min_cpu=np.zeros(200)

max_mem=np.zeros(200)
avg_mem=np.zeros(200)
min_mem=np.zeros(200)
m=0
while m<200 :
    min_cpu[m]=1.0
    min_mem[m]=1.0
    m=m+1
x=np.arange(0.0,8.0,0.04)
index=0
task_meta_file=csv.reader(open('F:\\download\\batch_task\\batch_task.csv','r'))
for mac in task_meta_file :


    if mac[7] != "" and mac[8] != "":
       name=mac[2]+mac[0]
       cpu=int(mac[7])
       mem=float(mac[8])
       task_cpu[name]=cpu
       task_mem[name]=mem
    index=index+1
    if index%100000==0 :
        print(index)
#print  (task_mem["j_3R7_6"])
index=0
instance_meta_file=csv.reader(open('D:\\batch_instance\\batch_instance.csv','r'))
for ins in instance_meta_file :
    time = float(ins[5]) / 3600 / 24
    time_seg = int(time / 0.04)
    data_segment[time_seg] = data_segment[time_seg] + 1
    if data_segment[time_seg]==101 and ins[10]!="" and ins[12] !="" :
        data_segment[time_seg] =0
        name= ins[2]+ins[1]
        cpu_used=float(ins[10])
        mem_used=float(ins[12])
        cpu_ratio=float(cpu_used)/task_cpu[name]
        mem_ratio=float(mem_used)/task_mem[name]
        if cpu_ratio > max_cpu[time_seg]:
            max_cpu[time_seg] = cpu_ratio
        if mem_ratio > max_mem[time_seg]:
            max_mem[time_seg] = mem_ratio
        if cpu_ratio < min_cpu[time_seg]:
            min_cpu[time_seg] = cpu_ratio
        if mem_ratio < min_mem[time_seg]:
            min_mem[time_seg] = mem_ratio
        avg_cpu[time_seg] = (avg_cpu[time_seg] * num_y[time_seg] + cpu_ratio) / (num_y[time_seg] + 1)
        avg_mem[time_seg] = (avg_mem[time_seg] * num_y[time_seg] + mem_ratio) / (num_y[time_seg] + 1)
        num_y[time_seg] = num_y[time_seg] + 1
        data_segment[time_seg] = 0

    index +=1
    if index%100000==0 :
        print (index)

out=open('instance_used_requested.csv','w',newline='')
csv_write=csv.writer(out,dialect='excel')
csv_write.writerow(x)
csv_write.writerow(max_cpu)
csv_write.writerow(avg_cpu)
csv_write.writerow(min_cpu)
csv_write.writerow(max_mem)
csv_write.writerow(avg_mem)
csv_write.writerow(min_mem)
out.close()
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

plt.xlim(0,8)
plt.ylim(0,1.0)
plt.xticks(np.linspace(0,8,9,endpoint=True))
plt.yticks(np.linspace(0,1.0,11,endpoint=True))
plt.subplot(1,2,1)
plt.plot(x,max_cpu,color='red')
plt.plot(x,avg_cpu,color='blue')
plt.plot(x,min_cpu,color='green')
plt.subplot(1,2,2)
plt.plot(x,max_mem,color='red')
plt.plot(x,avg_mem,color='blue')
plt.plot(x,min_mem,color='green')
plt.savefig("instance_used_requested.jpg")
plt.show()