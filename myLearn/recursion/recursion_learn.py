def tail_recursion(a):
    print(a)
    tail_recursion(a + 1)


tail_recursion(1)
