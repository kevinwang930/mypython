import numpy as np
import matplotlib.pyplot as plt
import datetime

x = [datetime.datetime(2010, 12, 1, 10, 0),
    datetime.datetime(2011, 1, 4, 9, 0),
    datetime.datetime(2011, 5, 5, 9, 0)]
y = [4, 9, 2]

ax = plt.subplot(111)
ax.bar(x, y,width = 5)
ax.bar(datetime.datetime(2010, 12, 2, 10, 0),10,width = 5)
ax.xaxis_date()

plt.show()