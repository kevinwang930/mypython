class base:
    pass

a = base()
t = a.t
a.t = 3
print(t)