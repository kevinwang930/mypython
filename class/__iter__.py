class test:
    def __init__(self) -> None:
        self.list = [1,2,3]

    def __iter__(self):
        for i in self.list:
            yield i

    

ins = test()

for i in ins:
    print(i)