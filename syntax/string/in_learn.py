while True:
    try:
        s = input()
        if s in 'reset':
            print('reset what')
        elif s in 'reset board':
            print('board fault')
        elif s in 'board add':
            print('where to add')
        elif s in 'board delete':
            print('no board at all')
        elif s in 'reboot backplane':
            print('impossible')
        elif s in 'backplane abort':
            print('install first')
        else:
            print('unknown command')
    except:
        break