import matplotlib.pyplot as plt  
import datetime  
from matplotlib.dates import DateFormatter
t=[datetime.datetime(2010, 12, 2, 22, 0),datetime.datetime(2010, 12, 2, 23, 0),datetime.datetime(2010, 12, 10, 0, 0),datetime.datetime(2010, 12, 10, 6, 0)]  
y=[4,6,9,3]  
interval=1.0/24.0  #1hr intervals, but maplotlib dates have base of 1 day  
ax = plt.subplot(111)  
ax.bar(t, y, width=interval)  
ax.xaxis_date()   
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)
plt.show()

