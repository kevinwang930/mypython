def lowerAlpha2num(c):
    if c in 'abc':
        return '2'
    if c in 'def':
        return '3'
    if c in 'ghi':
        return '4'
    if c in 'jkl':
        return '5'
    if c in 'mno':
        return '6'
    if c in 'pqrs':
        return '7'
    if c in 'tuv':
        return '8'
    if c in 'wxyz':
        return '9'

def upperAlphaShift(c):
    t = c.lower()
    if t == 'z':
        return 'a'
    else:
        return chr(ord(t)+1)

def parse(l):
    t = ''
    for c in l:
        if c.islower():
            t+=str(lowerAlpha2num(c))
        elif c.isupper():
            t+=upperAlphaShift(c)
        else:
            t+=c
    return t
pd = input()
print(parse(pd))
