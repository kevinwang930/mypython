class base:
    class interclass:
        def __init__(self) -> None:
            self.name = 'kevin'


in1 = base.interclass()
in2 = base()
print(in1.name)
print(in2.interclass().name)