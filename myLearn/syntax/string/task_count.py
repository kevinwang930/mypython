# 描述
# 输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。

# 本题包含多组输入。

# 数据范围：输入的字符串长度满足 

# 输入描述：
# 输入一行字符串，可以有空格

# 输出描述：
# 统计其中英文字符，空格字符，数字字符，其他字符的个数

while True:
    try:

        s = input()
        a = 0
        d = 0
        b = 0
        o = 0
        for c in s:
            if c.isalpha():
                a+=1
            elif c.isdigit():
                d+=1
            elif c == ' ':
                b+=1
            else:
                o+=1
        print(a)
        print(b)
        print(d)
        
        print(o)
    except:
        break