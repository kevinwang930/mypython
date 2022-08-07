a = [1,2,3]
def f(a):
    a.append(4)
f(a[:])
print(a)