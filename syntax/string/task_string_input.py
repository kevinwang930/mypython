#  输入 n 个整型数，统计其中的负数个数并求所有非负数的平均值，结果保留一位小数，如果没有非负数，则平均值为0
# 本题有多组输入数据，输入到文件末尾。 

neCount = 0
pCount = 0
pSum = 0

while True:
    try:
        n = int(input())
        if n <0:
            neCount+=1
        else:
            pCount +=1
            pSum+=n
        

    except EOFError:
        print(neCount)
        if pCount == 0:
            print(0.0)
        else:
            print(round(pSum/pCount,1))
    except Exception:
        break