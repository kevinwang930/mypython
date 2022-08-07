# lisp math parser
from sys import stdin

def parse(s):
    if s.isdigit():
        return int(s)
    if s[0]!='(' or s[-1] != ')':
        return 'error'
    op = ''
    op1 = ''
    op2 = ''
    index = 1
    start = end = 0
    for i in range(index,len(s)-1):
        if s[i] != ' ':
            if start == 0:
                start = i
        else:
            if start > 0:
                end = i-1
                break
    op = s[start:end+1]
    index = end+1
    start = end = 0
    nest = 0
    for i in range(index,len(s)-1):
        if s[i] == ' ' or s[i] == ')': #结束判断
            if start == 0:
                continue
            else:
                end = i - 1
                break
        elif s[i] == '(':    # nest判断
            start = i
            end = s.find(')',i)
            nest = 1
            break
        elif start == 0:   #开始判断
            start = i
        else:
            continue
    
    op1 = parse(s[start:end+1])
    op2 = parse(s[end+1:len(s)-1].strip())
    # print(op)
    # print(op1)
    # print(op2)

    if op == 'add':
        return op1 + op2
    if op == 'sub':
        return op1 - op2
    if op == 'mul':
        return op1 * op2
    if op == 'div':
        if op2 !=0:
            q,rem = divmod(op1,op2)
            return q
        else:
            return 'error'
        


    

while True:
    try:
        s = stdin.readline().strip()
        print(parse(s))
    except:
        break