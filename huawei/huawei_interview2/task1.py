# 输入0-9若干个数字组成最大值和最小值，用到所有输入。

#  3 2 1 4 0


s = [i for i in input().split()]

s = sorted(s)
# print(s)
zeros = 0
start = 0

# 最小值
for i in range(len(s)):
    if s[i] == '0':
        zeros +=1
    if s[i] > '0':
        start = i
        break
minI = s[start:]
for i in range(zeros):
    minI.insert(1,'0')

m = ''
for i in range(len(minI)):
    m += minI[i]

maxI = ''
for i in range(len(s)-1,-1,-1):
    maxI += s[i]
print(m)
print(maxI)