#动态规划经典题目
#nowcoder不能导入numpy模块，只能手工创建二维数组
#重点注意二维数据的创建方法，重点注意其横竖坐标，注意注意
#dp = [[1 for i in range(n+1)] for j in range(m+1)]，横坐标是 n, 竖坐标是m
while True:
    try:
        str1 = input()
        str2 = input()
        m = len(str1)
        n = len(str2)
         
        dp = [[1 for i in range(n+1)] for j in range(m+1)]#重点注意二维数据的创建方法，重点注意其横竖坐标，注意注意
        for i in range(n+1):
            dp[0][i] = i
        for j in range(m+1):
            dp[j][0] = j
             
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:#如果当前两个字母相同，则跳过，步数不增加
                    dp[i][j]=dp[i-1][j-1]
                else:  #如果两个字母不同，则有三种方式可以达成，删除、插入、替换，选择最小的前状态，步数加1
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
        print(dp[m][n])
    except:
        break