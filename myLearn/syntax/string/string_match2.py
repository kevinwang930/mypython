def include_first(s):
    length = -1
    for i in range(1,len(s)//2+1):
        s1= s[:i][::-1]
        s2 = s[i:]
        r = s2.find(s1)
        if s2.find(s1,1) == 1:
            length = i*2+1
        elif s2.find(s1) == 0:
            length = i*2
        
    if length >=0:
        return length
    else:
        return 0
        
def f(s):
    if len(s) == 0:
        return 0
    fi = include_first(s)
    fe = f(s[1:])
    return max(fi,fe)
s = input()
print(f(s))