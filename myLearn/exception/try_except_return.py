

def demo1():
    try:
        raise Exception('test')
    except Exception:
        return 2

    finally:
        return 1

def demo2():
    try:
        raise Exception('test')
        return 3
    except Exception:
        return 2

def demo3():
    try:
        return 3
        raise Exception('test')
        
    except Exception:
        return 1



print(demo1())
print(demo2())
print(demo3())
