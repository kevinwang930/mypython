from enum import Enum

class e(Enum):
    fail = 0
    pass1 = 1
    full = 2

a = e.fail

if a.value <= e.fail.value:
    print('enum fail')

print(type(a.name))



for item in e:
    print(item.name)