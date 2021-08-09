class base:
    def __init__(self) -> None:
        self._name = 'base'
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,namestr):
        self._name = namestr

class test(base):
    # def __init__(self) -> None:
    #     base.__init__(self)
    pass


t = test()
print(t.__dict__)
print(t.name)
t.name = 'test'
print(t.name)

print(dir(t))
print(t.__dict__)