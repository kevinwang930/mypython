def first_include_f(s1,s2):
    length = -1
    for i in range(1,len(s2)+1):
        if s1.find(s2[:i]) != -1:
            length = i
        else:
            break
    if length >= 0:
        return length
    else:
        return 0

def f(s1,s2):
    if len(s2) == 0:
        return 0
    else:
        fi = first_include_f(s1,s2)
        fe = f(s1,s2[1:])
        if fi > fe:
            return fi
        else:
            return fe

s1 = input()
s2 = input()
if len(s1) >= len(s2):
    print(f(s1,s2))
else:
    print(f(s2,s1))