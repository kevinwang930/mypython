class base:
    def __init__(self) -> None:
        self.name = 'kevin'

c = base()
t = getattr(c,'name')
c.name = 'wang'
print(t)
t = c.name
c.name = 'test'
print(t)
