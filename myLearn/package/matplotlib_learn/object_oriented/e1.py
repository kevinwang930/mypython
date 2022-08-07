from matplotlib import pyplot as plt
import numpy as np
import math
#figure 
fig=plt.figure(figsize=(6.4, 4.8),facecolor='skyblue', edgecolor='black')
# # fig = plt.figure()
# # ax = fig.add_axes([0,0,1,1])
# ax = fig.add_axes([0.1,0.1,0.8,0.8], projection='rectilinear',xlabel='X-label',ylabel='Y-label',title='Creating new Figure & Axes')
ax = fig.add_subplot(111,xlabel='X-label',ylabel='Y-label',title='Creating new Figure & Axes')
# fig, ax = plt.subplots()
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
# ax.text(0.5, 0.5, "middle of graph", transform=ax.transAxes)
ax.plot(x,y,color='black')
plt.show()