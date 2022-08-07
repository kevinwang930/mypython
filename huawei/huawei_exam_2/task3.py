#周长

import sys


def calcLength(l):
    length = 0
    for p in l:
        r,c = p
        if r == 0 or [r-1,c] not in l:   #上
            length+=1
        if r==63 or [r+1,c] not in l:
            length +=1
        if c == 0 or [r,c-1] not in l:
            length+=1
        if c ==63 or [r,c+1] not in l:
            length+=1
    return length


n = int(sys.stdin.readline().strip())

d = [[] for _ in range(n)]
r = [0 for _ in range(n)]
for i in range(n):
    m = [int(i) for i in sys.stdin.readline().strip().split()]
    for j in range(1,len(m)-1,2):
        pos = [m[j],m[j+1]]
        d[i].append(pos)
    
# print(d)

for i in range(n):
    r[i] = calcLength(d[i])
r = [str(i) for i in r]
print(' '.join(r))

