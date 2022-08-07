l = [1,2,3,4,5,6]

del l[0:1]

l.pop(l.index(2))

l.remove(3)


print(l)
l.clear()
print(l)
l.remove(3)