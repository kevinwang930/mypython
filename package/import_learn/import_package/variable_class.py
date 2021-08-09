class test:
    def __init__(self) -> None:
        self.a = 1
    
ins = test()
def test_a():
    ins.a = 2

if __name__ == '__main__':
    print(ins.a)
    test_a()
    print(ins.a)