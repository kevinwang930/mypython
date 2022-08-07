def dec(f,*args,**kwargs):
    print('this is decorator')
    print(*args)
    print(**kwargs)
    f(*args,**kwargs)
    return f

@dec
def func(a=1,b=1):
    print(f'this is func {a+b}')

