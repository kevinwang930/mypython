class Vformat:
    def __init__(self) -> None:
        self.a = 'b'
        self.format = str


v = Vformat()
v.a = 1
print(type(v.format(v.a)))
