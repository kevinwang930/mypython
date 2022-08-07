# variable gc
import sys
a = 'my string'
c = sys.getrefcount(a)
print(c)

b = 'my string'
f = 'my string'


print(id(b),id(f))

del b
del 'my string'

c = sys.getrefcount('my string')
print(c)

