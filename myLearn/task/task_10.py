# 正则表达式

s = input()
p = input()

class Solution:

    def isMatch(self,s,p):
        len_s = len(s)
        len_p = len(p)
        dp = dict()

        def match(i,j):
            # 结束判断 同时结束为True
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i==len_s:
                if j==len_p:
                    dp[(i,j)] = True
                    return True
                    # 超过两个字符
                if len_p - j >=2:
                    if p[j+1]=='*':
                        return match(i,j+2)
                    dp[(i,j)] = False
                    return False
                dp[(i,j)] = False
                return False
                
                
            if j ==len_p:
                return False
            if p[j].isalpha():
                if len_p-j >=2 and p[j+1]=='*':
                    if p[j]==s[i]:
                        return match(i,j+2) or match(i+1,j)
                    return match(i,j+2)
                if p[j]==s[i]:
                    return match(i+1,j+1)
                return False
            if p[j] == '.':
                if len_p-j >=2 and p[j+1]=='*':
                    return match(i,j+2) or match(i+1,j)
                return match(i+1,j+1)
        return match(0,0)

    def isMatch1(self,s,p):
        len_s = len(s)
        len_p = len(p)
        dp = [[False]*len_p for _ in range(len_s)]
        dp[0][0]= True

        for i in range(1,len_s):
            for j in range(1,len_p):
                if s[i] == p[j]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    if p[j-1].isalpha():
                        if s[i] == p[j-1]:  #字母相同至少匹配一次
                            dp[i][j] = dp[i-1][j]
                        dp[i][j] = dp[i][j-2] #字母不同匹配0次
                    elif p[j-1] == '.':
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
        return dp[len_s-1][len_p-1]

s1 = Solution()
print(s1.isMatch(s,p))