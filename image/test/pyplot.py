
import matplotlib.pyplot as plt #绘图用的模块
from mpl_toolkits.mplot3d import Axes3D #绘制3D坐标的函数
import numpy as np
import time
 
# %% 使用的绘图抛物曲面
def fun(x,y):
    return np.power(x,2)+np.power(y,2)
 

# %% 绘图数据准备
X=np.arange(-2,2,0.1)
Y=np.arange(-2,2,0.1)#创建了从-2到2，步长为0.01的arange对象
X,Y=np.meshgrid(X,Y)
Z=fun(X,Y)#用取样点横纵坐标去求取样点Z坐标

# %% 绘图耗时计时
t1 = time.time()
fig1=plt.figure()#创建一个绘图对象
ax=Axes3D(fig1)#用这个绘图对象创建一个Axes对象(有3D坐标)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.cool)#用取样点(x,y,z)去构建曲面
ax.set_xlabel('x label', color='r')
ax.set_ylabel('y label', color='g')
ax.set_zlabel('z label', color='b')#给三个坐标轴注明
plt.title("This is main title")#总标题

t2 = time.time()
print('take time {:.5f} seconds\n'.format(t2-t1))
plt.show()
