while True:
    try:
        n = int(input())

        if n <= 2:
            print(-1)
        elif n%2 == 1:
            print(2)
        elif (n-2)%4 == 0:
            print(4)
        else:
            print(3)
    except:
        break
    