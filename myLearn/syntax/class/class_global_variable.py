name = 'kevin'
class base:
    def test(self):
        global name
        name = name + 'test'
        print(name)

t = base()
t.test()
print(name)