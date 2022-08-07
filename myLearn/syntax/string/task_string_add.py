# 输入两个用字符串 str 表示的整数，求它们所表示的数之和。

def s_sum(s1,s2):
    a1 = list(s1)
    a1.reverse()
    a2 = list(s2)
    a2.reverse()
    l1 = len(s1)
    l2 = len(s2)
    if l1 >= l2:
        long = a1
        short = a2
    else:
        long = a2
        short = a1
    long_key = len(long)
    short_key = len(short)
    r = [0 for _ in range(long_key+1)]
    inc = 0
    for i in range(short_key):
        inc,r[i]= divmod(int(long[i]) + int(short[i])+inc,10)
    
    for i in range(short_key,long_key):
        inc,r[i]= divmod(int(long[i]) +inc,10)
    if inc ==1 :
        r[long_key] = 1
    else:
        r.pop()
    r.reverse()
    r = map(str,r)
    return ''.join(r)



while True:
    try:
        a = input()
        b = input()
        print(s_sum(a,b))
    except Exception as e:
        break