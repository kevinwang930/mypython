#__getitem__ legacy feature supports for
class test:
    def __init__(self) -> None:
        self.list = [1,2,3]

    def __getitem__(self,key):
        return self.list[key]

    

ins = test()
print(ins[2])

for i in ins:
    print(i)