class testBase:
    @classmethod
    def onEntry(cls):
        print('this is base entry method')

    @staticmethod
    def statictest():
        print('this is in static method')

class test1(testBase):
    
    def __init__(self) -> None:
        pass




test1.onEntry()
ins1 = testBase()
ins1.statictest()
ins2 = test1()
ins2.statictest()