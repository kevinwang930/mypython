class meta(type):
    pass
    

def construct(self) -> None:
    self.name = 'kevin'
construct.__name__ = "__init__"
bases = ()
dict = {}
dict['__init__'] = construct
base = meta('base',bases,dict)



b = base()
print(b.name)
