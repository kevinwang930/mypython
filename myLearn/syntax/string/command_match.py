commands = {
    'reset':"reset what",
    'reset board':'board fault',
    'board add':'where to add',
    'board delete':'no board at all',
    'reboot backplane':'impossible',
    'backplane abort':'install first',
}


def match_command(*args):
    args_count = len(args)
    targets = []
    
    for key,value in commands.items():
        keyWords = key.split()
        if len(keyWords) != args_count:
            continue
        flag = 1
        for i in range(args_count):
            if keyWords[i].find(args[i]) != 0:
                flag = 0
                break
        if flag == 1:
            targets.append(value)

    if len(targets) == 1:
            return targets[0]
    else:
        return 'unknown command'


                        
                        
    
        
while True:
    try:
        c = input().split()
        print(match_command(*c))
    except Exception as e:
        print(e)
        break