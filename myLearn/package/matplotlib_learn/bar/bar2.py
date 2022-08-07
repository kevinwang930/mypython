import numpy as np
import matplotlib.pyplot as plt

#The data
womenMeans = (25, 32, 34, 20, 25)
menMeans = (20, 35, 30, 35, 27)
indices = [5.5,6,7,8.5,8.9]
#Calculate optimal width
width = np.min(np.diff(indices))/3

fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(indices-width,womenMeans,width,color='b',label='-Ymin')
ax.bar(indices,menMeans,width,color='r',label='Ymax')
ax.set_xlabel('Test histogram')
plt.show()