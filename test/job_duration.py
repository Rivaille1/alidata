import numpy as np
import matplotlib.pyplot as plt
import csv
import random
import re
import pandas
import math
task_meta_file=csv.reader(open('F:\\download\\batch_task\\batch_task.csv','r'))
task_job_start=dict()
task_job_end=dict()
task_job_time=dict()
index=0
for mac in task_meta_file :
    if mac[4]=="Terminated":
        job_name=mac[2]
        start_time=int(mac[5])
        end_time=int(mac[6])
        if task_job_start.__contains__(job_name):
             if task_job_start[job_name]>start_time :
                 task_job_start[job_name]=start_time
             if task_job_end[job_name]<end_time:
                 task_job_end[job_name]=end_time
        else :
            task_job_start[job_name] = start_time
            task_job_end[job_name]=end_time
    index=index+1
    if index%100000==0 :
        print(index)
job_time=[]
for key in task_job_start :
    tmp=task_job_end[key]-task_job_start[key]
    if tmp<0 :
        break
    tmp=float(tmp/3600)
    task_job_time[key]=tmp
    job_time.append(tmp)
job_time.sort()
job_time_dict=dict()
sum=len(job_time)
i=0
while i<len(job_time) :
    if job_time_dict.__contains__(job_time[i]):
        job_time_dict[job_time[i]]+=1
    else:
        job_time_dict[job_time[i]]=1
    i=i+1
plotDatasetx=[]
plotDatasety=[]
last=0
print (job_time_dict)
for key in job_time_dict :
    if key ==0 :
        plotDatasetx.append(-4)
        plotDatasety.append(0)
        last=last+job_time_dict[key]
        continue

    plotDatasetx.append(math.log(key,10))
    plotDatasety.append((job_time_dict[key]+last)/sum)
    last=last+job_time_dict[key]
plt.xlim(-4,1.5)
plt.ylim(0.0,1.0)
plt.xticks(np.linspace(-4,1,5),('10^-4','10^-3','10^-2','10^-1','10^0','10^1'))
plt.xlabel('job_duration(hour)')
plt.ylabel('portion of jobs')
plt.plot(plotDatasetx,plotDatasety, '-', linewidth=2,color='red')
plt.savefig("job_duration.jpg")

plt.show()
