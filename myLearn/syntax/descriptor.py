


class Property(object):
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    # def getter(self, fget):
    #     return type(self)(fget, self.fset, self.fdel, self.__doc__)

    # def setter(self, fset):
    #     return type(self)(self.fget, fset, self.fdel, self.__doc__)

    # def deleter(self, fdel):
    #     return type(self)(self.fget, self.fset, fdel, self.__doc__)


class Property2(object):
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, initVal):
        self._x = initVal

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self._x

    def __set__(self, obj, value):
        self._x = value

    def __delete__(self, obj):
        del self._x

class C(object):
    def __init__(self):
        self.__x = 10


    def getx(self): return self.__x
    def setx(self, value): self.__x = value

    def delx(self): del self.__x
    x = Property(getx, setx, delx, "I'm the 'x' property.")
    x2 = Property2(100)
    


instance = C()
print(instance.x)
print(instance.x2)
instance.x2 = 1000
ins2 = C()
print(ins2.x2)


class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val


class MyClass(object):


    x = RevealAccess(10, 'var "x"')
    y = 5


c = MyClass()
print(c.x)

