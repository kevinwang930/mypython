
def lazy_range(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive."""
    index = 0
    while index < up_to:
        result = yield index
        print('result after yield',result)
        if isinstance(result,int):
            
            index = result
        else:
            index += 1

r = lazy_range(100)
print(next(r))
print(next(r))
print(r.send(0))
print(next(r))


def lazy_range(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive."""
    index = 0
    def gratuitous_refactor():
        nonlocal index
        while index < up_to:
            yield index
            index += 1
    yield from gratuitous_refactor()

r = lazy_range(100)
print(next(r))
print(next(r))

# Using the generator pattern (an iterable)
class first_n(object):


    def __init__(self, n):
        self.n = n
        self.num = 0


    def __iter__(self):
        return self


    # Python 3 compatibility
    def __next__(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        raise StopIteration()

    def send(self,num):
        self.num = num



    # def next(self):
    #     if self.num < self.n:
    #         cur, self.num = self.num, self.num+1
    #         return cur
    #     raise StopIteration()


sum_of_first_n = sum(first_n(1000000))

print(sum_of_first_n)

test = first_n(100)
test.send(50)
print(next(test))