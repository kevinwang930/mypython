# 蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。

# 例如，当输入5时，应该输出的三角形为：

# 1 3 6 10 15

# 2 5 9 14

# 4 8 13

# 7 12

# 11


# 请注意本题含有多组样例输入。

while True:
    try:
        d = int(input())
        r = [[] for _ in range(d)]
        # print(r)
        n = 1
        for l in range(d):
            for i in range(l,-1,-1):
                r[i].append(n)
                n+=1
        for i in r:
            print(" ".join([str(j) for j in i]))
    except:
        break


