def func_out(x):
    def func_inner():
        nonlocal x
        x = x * 10
        print(x)
    return func_inner

a = func_out(1)
a()
a()

