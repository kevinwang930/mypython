while True:
    try:
        
        s = input()
        c = 0
        checked = set()
        for i in range(len(s)):
            if s[i] not in checked and s.find(s[i],i+1) == -1:
                c = s[i]
                break
            checked.add(s[i])
        if c == 0:
            print(-1)
        else:
            print(c)
    except:
        break