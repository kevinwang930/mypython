# descriptor let objects customize attribute lookup,storage and deletion.

class Ten:
    def __get__(self, obj, objtype=None):
        return 10

    

class A:
    x = 5                       # Regular class attribute
    y = Ten()                   # Descriptor instance

a = A()
print(a.x)
print(a.y)