while True:
    try:
        s = list(input())
        for i in range(len(s)):
            if s[i].isalpha():
                for j in range(i+1,len(s)):
                    if s[j].isalpha() and s[j].upper() < s[i].upper():
                        m = s[i]
                        s[i] = s[j]
                        s[j] = m
        print(''.join(s))
    except:
        break