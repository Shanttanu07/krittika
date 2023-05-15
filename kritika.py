import numpy as np
import matplotlib.pyplot as plt
file1=open(r"event_Q1.txt","r")
line=file1.readline()
time_stamps=line.split(",")
a=[]
for i in range(len(time_stamps)):
  if float(time_stamps[i])>0:
    a.append(time_stamps[i])
print(len(a))
a.sort()
max=float(a[0])
for i in range(len(a)):
    if(float(a[i])>max):
        max=float(a[i])
    
b=[]
for i in range(int(max) +1):
    b.append(0)
    for k in range(len(a)):
        if float(a[k])>=i and float(a[k])<i+1:
            b[i]+=1
y=[]
for i in range(int(max)+1):
    y.append(i)
    
file4=open(r"event_Q4.txt","r")
line3=file4.readline()
time_stamps3=line3.split(",")
a3=[]
for i in range(len(time_stamps3)):
  if float(time_stamps3[i])>0:
    a3.append(time_stamps3[i])
print(len(a3))
a3.sort()
max3=float(a3[0])
for i in range(len(a3)):
    if(float(a3[i])>max3):
        max3=float(a3[i])
    
b3=[]
for i in range(int(max3) +1):
    b3.append(0)
    for k in range(len(a3)):
        if float(a3[k])>=i and float(a3[k])<i+1:
            b3[i]+=1
y3=[]
for i in range(int(max3)+1):
    y3.append(i)

file3=open(r"event_Q3.txt","r")
line2=file3.readline()
time_stamps2=line2.split(",")
a2=[]
for i in range(len(time_stamps2)):
  if float(time_stamps2[i])>0:
    a2.append(time_stamps2[i])
print(len(a2))
a2.sort()
max2=float(a2[0])
for i in range(len(a2)):
    if(float(a2[i])>max2):
        max2=float(a2[i])
    
b2=[]
for i in range(int(max2) +1):
    b2.append(0)
    for k in range(len(a2)):
        if float(a2[k])>=i and float(a2[k])<i+1:
            b2[i]+=1
y2=[]
for i in range(int(max2)+1):
    y2.append(i)
    
file2=open(r"event_Q2.txt","r")
line1=file2.readline()
time_stamps1=line1.split(",")
a1=[]
for i in range(len(time_stamps1)):
  if float(time_stamps1[i])>0:
    a1.append(time_stamps1[i])
print(len(a1))
a1.sort()
max1=float(a1[0])
for i in range(len(a1)):
    if(float(a1[i])>max1):
        max1=float(a1[i])
    
b1=[]
for i in range(int(max1) +1):
    b1.append(0)
    for k in range(len(a1)):
        if float(a1[k])>=i and float(a1[k])<i+1:
            b1[i]+=1
y1=[]
for i in range(int(max1)+1):
    y1.append(i)
    

plt.xlabel("time span")
plt.ylabel("frequency of events")
plt.plot(y,b)
plt.plot(y1,b1)
plt.plot(y2,b2)
plt.plot(y3,b3)
plt.legend(["line1","line2","line3","line4"])
plt.show()
bins=0
min=[max,max1,max2,max3]
min.sort()
min_time=min[0]
for i in range(int(min_time)):
    counter=0
    if(b[i]>140):
        counter+=1
    if(b1[i]>140):
        counter+=1
    if(b2[i]>140):
        counter+=1
    if(b2[i]>140):
        counter+=1
    if(counter>1):
        bins+=1
print(bins)
bin1=[]
bin2=[]
bin3=[]
bin4=[]
for k in range(7):
    bin1.append(0)
    for i in range(int(min_time)):
        counter=0
        if(b[i]>k*5+140):
            counter+=1
        if(b1[i]>k*5+140):
            counter+=1
        if(b2[i]>k*5+140):
            counter+=1
        if(b2[i]>k*5+140):
            counter+=1
        if(counter>0):
            bin1[k]+=1
for k in range(7):
    bin2.append(0)
    for i in range(int(min_time)):
        counter=0
        if(b[i]>k*5+140):
            counter+=1
        if(b1[i]>k*5+140):
            counter+=1
        if(b2[i]>k*5+140):
            counter+=1
        if(b2[i]>k*5+140):
            counter+=1
        if(counter>1):
            bin2[k]+=1
            
for k in range(7):
    bin3.append(0)
    for i in range(int(min_time)):
        counter=0
        if(b[i]>k*5+140):
            counter+=1
        if(b1[i]>k*5+140):
            counter+=1
        if(b2[i]>k*5+140):
            counter+=1
        if(b2[i]>k*5+140):
            counter+=1
        if(counter>2):
            bin3[k]+=1

for k in range(7):
    bin4.append(0)
    for i in range(int(min_time)):
        counter=0
        if(b[i]>k*5+140):
            counter+=1
        if(b1[i]>k*5+140):
            counter+=1
        if(b2[i]>k*5+140):
            counter+=1
        if(b2[i]>k*5+140):
            counter+=1
        if(counter>4):
            bin4[k]+=1



dict={1:bin1,2:bin2,3:bin3,4:bin4}
print(dict)


          

        



