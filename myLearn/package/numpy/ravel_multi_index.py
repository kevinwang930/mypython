import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
index = np.ravel_multi_index(arr, (4,8))
print(index)
id1,id2 = np.unravel_index(index,(4,8))
print(id1,id2)
print(type(id1))