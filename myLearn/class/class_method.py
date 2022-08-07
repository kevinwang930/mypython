class testBase:
    @classmethod
    def onEntry(cls):
        print('this is base entry method')

class test1(testBase):
    
    def __init__(self) -> None:
        pass


    def onEntry(self):
        print('this is advanced entry method')

instance = test1()

instance.onEntry()
testBase.onEntry()

