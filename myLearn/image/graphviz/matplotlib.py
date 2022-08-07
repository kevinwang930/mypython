# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 21:58:33 2020

@author: kevin
"""
#pyplot module state machine environment
#object-oriented interface figure and axe 
# sphinx_gallery_thumbnail_number = 3
import pandas 
import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure()  # an empty figure with no axes
# fig.suptitle('No axes on this figure')  # Add a title so we know which it is

# fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes


# a = pandas.DataFrame(np.random.rand(4,5), columns = list('abcde'))
# a_asarray = a.values

# x = np.linspace(0, 2, 101)

# plt.plot(x, x, label='linear')
# plt.plot(x, x**2, label='quadratic')
# plt.plot(x, x**3, label='cubic')

# plt.xlabel('x label')
# plt.ylabel('y label')

# plt.title("Simple Plot")

# plt.legend()

# plt.show()


#new example

x = np.arange(0, 10, 0.2)
y = np.sin(x)

fig = plt.figure()
ax = plt.subplot(2,2,2)
ax.plot(x, y)
ax = plt.subplot(2,2,1)
ax.plot(x, y)
plt.show()

