import matplotlib.pyplot as plt
import numpy as np
x = np.arange(11)
fig = plt.figure()
ax1 = fig.add_subplot(3,1,1)  
ax1.plot(x,x)  
ax2 = fig.add_subplot(3,1,2,sharex= ax1)  
ax2.plot(x,x*2)


plt.show()