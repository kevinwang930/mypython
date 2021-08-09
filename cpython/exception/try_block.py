try:
    raise Exception("this is an exception")
except Exception as e:
    print(e)