# 给出一个名字，该名字有26个字符组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
# 每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个不同字母拥有相同的“漂亮度”。字母忽略大小写。

# 给出多个名字，计算每个名字最大可能的“漂亮度”。

# 本题含有多组数据。

def b(s):
    l = []
    counted = ''
    for c in s:
        if c in counted:
            continue
        q = s.count(c)
        counted+=c
        l.append([c,q])
    l.sort(key=lambda x:x[1],reverse=True)
    w = 26
    tw = 0
    for e in l:
        tw += w*e[1]
        w-=1
    return tw



name_count = int(input())
for i in range(name_count):
    n = input()
    print(b(n))
   