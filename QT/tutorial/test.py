class Foo:
    def __init__(self):
        self.i = 1
    def __call__(self):
        print('called')

foo_instance = Foo()
foo_instance() #this is calling the __call__ method
print(foo_instance.i)
foo_instance.i = 10
print(foo_instance.i)
foo2=Foo()
print(foo2.i)