a = [1,2,3]
print(a[1])
# print(list.__dict__)
a.extend([4,5,6])
a.append(7)
print(a)
x ='c'
a[0]=x
b = a[:]
x= 'z'
print(b)