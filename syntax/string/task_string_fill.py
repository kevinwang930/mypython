#  •连续输入字符串，请按长度为8拆分每个输入字符串并进行输出；
# •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
# （注：本题有多组输入）

while True:
    try:
        s = input()
        for i in range(0,len(s),8):
            if i+7 < len(s):
                print(s[i:i+8])
            else:
                l =  s[i:].ljust(8,'0')
                print(l)
                break

    except:
        break