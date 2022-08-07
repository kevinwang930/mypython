# 【面试题】求连续子数组的最大和 
# 给定一个数组 array[1, 4, -5, 9, 8, 3, -6]，在这个数字中有多个子数组，子数组和最大的应该是：[9, 8, 3]，输出20，再比如数组为[1, -2, 3, 10, -4, 7, 2, -5]，和最大的子数组为[3, 10, -4, 7, 2]，输出18。
# 


s = [1, -2, 3, 10, -4, 7, 2, -5]

n = len(s)
maxSum = s[0]

dp = [s[i] for i in range(n)]

for i in range(len(s)):
    dp[i][i] = s[i]

# for i in range(len(s)):
#     for j in range(i,len(s)):
#         if i == j:
#             if s[i] > maxSum:
#                 maxSum = s[i]
#         else:
#             sum = 0
#             for k in range(i,j+1):
#                 sum += s[k]
#             if sum > maxSum:
#                 maxSum = sum

for i in range(len(s)):
    dp
        



print(maxSum)

