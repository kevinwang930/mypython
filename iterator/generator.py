def gratuitous_refactor(up_to):
        index = 0
        while index < up_to:
            jump = yield index
            if jump is None:
                jump = 1
            index += jump

# def lazy_range(up_to):
#     """Generator to return the sequence of integers from 0 to up_to, exclusive."""
#     # index = 0
    
#     yield from gratuitous_refactor(up_to)

if __name__ == '__main__':
    # iterator = lazy_range(5)
    # print(next(iterator))  # 0
    # print(iterator.send(2))  # 2
    # print(next(iterator))  # 3
    # print(iterator.send(-1))  # 2
    # for x in iterator:
    #     print(x)  # 3, 4

    iterator = gratuitous_refactor(5)
    print(next(iterator))  # 0
    # print(iterator.send(2))  # 2
    # print(next(iterator))  # 3
    # print(iterator.send(-1))  # 2
    # for x in iterator:
    #     print(x)  # 3, 4
