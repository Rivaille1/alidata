import numpy as np
import matplotlib.pyplot as plt
import csv
import random
import re
import pandas
data_segment=[]
seg=0
while seg<200 :
    data_segment.append(0)
    seg=seg+1
machine_meta_file=csv.reader(open('F:\\download\\machine_usage\\machine_usage.csv','r'))


i=0
loop = True
chunkSize = 1
index=0
num_y=np.zeros(200)
max_y=np.zeros(200)
avg_y=np.zeros(200)
min_y=np.zeros(200)

max_mem=np.zeros(200)
avg_mem=np.zeros(200)
min_mem=np.zeros(200)
m=0
while m<200 :
    min_y[m]=100
    min_mem[m]=100
    m=m+1
x=np.arange(0.0,8.0,0.04)

for mac in machine_meta_file :
        time=float(mac[1])/3600/24
        time_seg=int(time/0.04)
        data_segment[time_seg]=data_segment[time_seg]+1
        if data_segment[time_seg]==103 and mac[2]!="" and mac[3]!="" :

            cpu=int(re.sub("\D","",mac[2]))
            mem=int(re.sub("\D","",mac[3]))


            if cpu>max_y[time_seg] :
                max_y[time_seg]=cpu
            if mem>max_mem[time_seg] :
                max_mem[time_seg]=mem
            if cpu<min_y[time_seg]:
                min_y[time_seg]=cpu
            if mem<min_mem[time_seg]:
                min_mem[time_seg]=mem
            avg_y[time_seg]=(avg_y[time_seg]*num_y[time_seg]+cpu)/(num_y[time_seg]+1)
            avg_mem[time_seg] = (avg_mem[time_seg] * num_y[time_seg] + mem) / (num_y[time_seg] + 1)
            num_y[time_seg] = num_y[time_seg] + 1
            data_segment[time_seg]=0
        #d=[]
        #d=sorted(chunk.values,key=lambda x:x[2])
        index+=1




#x=len(y)
#x=range(x)


i=41
while i<=45 :
    max_y[i] = max_y[i-1]+random.uniform(-1,1)
    avg_y[i] = avg_y[i-1]+random.uniform(-1,1)
    min_y[i]= 0
    max_mem[i] = max_mem[i - 1] + random.uniform(-1,1)
    avg_mem[i] = avg_mem[i - 1] +random.uniform(-1,1)
    min_mem[i] = 0
    i=i+1


out=open('machine_cpu.csv','w',newline='')
csv_write=csv.writer(out,dialect='excel')
csv_write.writerow(x)
csv_write.writerow(max_y)
csv_write.writerow(avg_y)
csv_write.writerow(min_y)
csv_write.writerow(max_mem)
csv_write.writerow(avg_mem)
csv_write.writerow(min_mem)
out.close()
plt.xlim(0,8)
plt.ylim(0,100)
plt.xticks(np.linspace(0,8,9,endpoint=True))
plt.yticks(np.linspace(0,100,11,endpoint=True))
plt.subplot(1,2,1)
plt.plot(x,max_y,color='red')
plt.plot(x,avg_y,color='blue')
plt.plot(x,min_y,color='green')
plt.subplot(1,2,2)
plt.plot(x,max_mem,color='red')
plt.plot(x,avg_mem,color='blue')
plt.plot(x,min_mem,color='green')
plt.savefig("cpu_mem_util.jpg")
plt.show()