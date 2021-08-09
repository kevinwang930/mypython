nolocal1 = 1
def testfunc(a):
    b = a + nolocal1 + 1
    return b

c = testfunc(1)

