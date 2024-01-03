#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import csv
x = []
y = []

with open("CV_values.txt",'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
plt.plot(x,y, label='Loaded from file')

plt.xlabel('Raman Shift in cm-1')
plt.ylabel('Raman Intensity in cm-1')
plt.title(' ')
plt.legend()
plt.show()


# In[ ]:





# In[7]:


lst = [0,0,0,0,0,0,0,0,0]
for i in x:
    if(i in range(415,425)):
        lst[0] = 1
    elif(i in range(435,445)):
        lst[0] = 1
    elif(i in range(795,805)):
        lst[0] = 1
    elif(i in range(910,920)):
        lst[0] = 1
    elif(i in range(1210,1225)):
        lst[0] = 1
    elif(i in range(1170,1177)):
        lst[0] = 1
    elif(i in range(1360,1375)):
        lst[0] = 1
    elif(i in range(1610,1620)):
        lst[0] = 1
    
ans = 1
for i in range(0,len(lst)):
    if(lst[i] == 1):
        ans = 0
        break
if(ans):
    print("Crystal Violet")


# In[8]:


import matplotlib.pyplot as plt
import csv
x = []
y = []

with open("values.txt",'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
plt.plot(x,y, label='Loaded from file')

plt.xlabel('Raman Shift in cm-1')
plt.ylabel('Raman Intensity in cm-1')
plt.title('')
plt.legend()
plt.show()


# In[2]:


lst = [0,0,0,0,0,0,0,0,0]
for i in x:
    if(i in range(600,615)):
        lst[0] = 1
    elif(i in range(760,775)):
        lst[0] = 1
    elif(i in range(1120,1135)):
        lst[0] = 1
    elif(i in range(1175,1190)):
        lst[0] = 1
    elif(i in range(1305,1320)):
        lst[0] = 1
    elif(i in range(1355,1365)):
        lst[0] = 1
    elif(i in range(1500,1515)):
        lst[0] = 1
    elif(i in range(1595,1603)):
        lst[0] = 1
    elif(i in range(1640,1653)):
        lst[0] = 1
ans = 1
for i in range(0,len(lst)):
    if(lst[i] == 1):
        ans = 0
        break
if(ans):
    print("Rhodamine - 6g")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




