import dis
def test(l = []):
    l.append('kevin')
    print(l)

test()
test()

def test2(a = 1):
    a = a+1
    print(a)

test2()
test2()

dis.dis(test)