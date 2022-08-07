# 字符串相邻反复消除

import sys

def removeDuplicate(s):
    if len(s)<=1:
        return 0,s
    flag = 0
    returnValue = ''
    i = 0
    for i in range(len(s)):
        if i == len(s)-1:
            return 0,s
        if not s[i].isalpha():
            return 0,''
        if s[i] == s[i+1]:
            return 1,s[:i]+s[i+2:]



s = sys.stdin.readline().strip()
flag = 1
while flag:
    flag,s = removeDuplicate(s)
print(len(s))
    

