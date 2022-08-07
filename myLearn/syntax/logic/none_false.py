def test():
    return False
b = False

if test() is None:
    print('false is none')

if test() is False:
    print('false returned')

if b is None:
    print('none is none')