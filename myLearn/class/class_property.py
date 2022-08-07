class inner:
    a = 1
class test:
    i = inner()


x = test()
y = test()
x.i.a = 2
print(y.i.a)
