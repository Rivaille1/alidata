# coding=utf-8
from matplotlib import pyplot as plt
import numpy as np
from pylab import *
import csv
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

X = []
Z = []
Y = []
i = 0
j = 0
while j<4034 :
  while i<4000 :
    Y.append(0)
    i = i + 1
  i = 0
  X.append(Y)
  Z.append(Y)
  Y = []
  j = j + 1
index = 0
machine_meta_file=csv.reader(open('F:\\download\\machine_usage\\machine_usage.csv','r'))
for mac in machine_meta_file :
        machine_id=int(mac[0][2:])

        time=float(mac[1])
        time_seg=int(time/3456)
        if index%101==0 and mac[2] != "" and mac[3] != "":
           cpu=int(re.sub("\D","",mac[2]))
           mem=int(re.sub("\D","",mac[3]))
           tmp=0
           while tmp<20 :
              X[machine_id-1][time_seg*20+tmp]=cpu
              Z[machine_id-1][time_seg*20+tmp]=mem
              tmp=tmp+1


        #d=[]
        #d=sorted(chunk.values,key=lambda x:x[2])
        index+=1
        if index %100000==0 :
            print (index)


out=open('machine_hot.csv','w',newline='')
csv_write=csv.writer(out,dialect='excel')
i=0
while i<4034 :
    csv_write.writerow(X[i])
    i=i+1
i=0
while i<4034:
    csv_write.writerow(Z[i])
    i=i+1

out.close()





plt.ylim(0,4100)
plt.xlim(0,4000)
plt.xticks(np.linspace(0,4000,9,endpoint=True),('0','1','2','3','4','5','6','7','8'))
plt.yticks(np.linspace(0,4100,11,endpoint=True))

plt.subplot(1,2,1)
imshow(X,cmap=plt.cm.autumn,vmax=100,vmin=0,interpolation='nearest')
colorbar()


plt.subplot(1,2,2)
imshow(Z,cmap=plt.cm.autumn,vmax=100,vmin=0,interpolation='nearest')
colorbar()


savefig("hot.jpg")
show()


