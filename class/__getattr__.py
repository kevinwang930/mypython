from typing import Any

class base:
    def __init__(self) -> None:
        self.a = 10

    def test(self):
        print('this is a test function')

    def __getattr__(self,name):
        print(f'{name} is not defined in base')
        return None

    def __getattribute__(self, name: str) -> Any:
        print('I give you 10')
        return 10

t = base()
t.test()