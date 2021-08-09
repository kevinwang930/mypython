class base:
    def __init__(self) -> None:
        self.a = 1

    def __enter__(self):
        return self.a

    def __exit__(self, exc_type, exc_value, exc_traceback):  
        print('exit method called')  

with base() as a:
    print(a)