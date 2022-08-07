a = None
b = None
if a is None and b is None:
    print('None checked')

if not a and not b:
    print('None checked')

if not (a and b):
    print('None checked')

if a is False:
    print('False checked')

l = []
if l:
    print('empty list is not None')

c = 1
if c is 1:
    print('1 is 1')
    print(id(1))