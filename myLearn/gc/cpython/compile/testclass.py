class testclass0:
    firstname = 'wang'
    def __init__(self):
        """this is a doc string"""
        print('init running')
        self.name = 'kevin'
    def displayname(self):
        print(self.name)


a = testclass0()
a.displayname()
# print(testclass0.__classcell__)
