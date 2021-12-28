# 描述
# Levenshtein 距离，又称编辑距离，指的是两个字符串之间，由一个转换成另一个所需的最少编辑操作次数。许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。编辑距离的算法是首先由俄国科学家 Levenshtein 提出的，故又叫 Levenshtein Distance 。

# Ex：

# 字符串A: abcdefg

# 字符串B: abcdef

# 通过增加或是删掉字符 ”g” 的方式达到目的。这两种方案都需要一次操作。把这个操作所需要的次数定义为两个字符串的距离。

# 要求：

# 给定任意两个字符串，写出一个算法计算它们的编辑距离。


# 数据范围：给定的字符串长度满足 

# 本题含有多组输入数据。

def lev(s1,s2):

    pass

while True:
    try:
        s1 = input()
        s2 = input()
        m = len(s1)
        n = len(s2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1,dp[i-1][j]+1,dp[i][j-1]+1)
            
        
        print(dp[m][n])
    except:
        break

