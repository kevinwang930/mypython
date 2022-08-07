# 题目描述：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1个 或 2 个 或 3个台阶。你有多少种不同的方法可以爬到楼顶呢 ========== 示例1： 输入：n = 3 输出：4 说明: 有四种走法 ========== 示例 2： 输入：n = 5 输出：13 

t = int(input())
s = [1,2,3]
minS = 1
maxS = 3

# def calcM(total,l):
#     if len(l) > 0 :
#         if total < l[0]:
#             return calcM(total,l[1:])
#         if total == l[0]:
#             return 1 + calcM(total,l[1:])
#         return calcM(total - l[0],l)+calcM(total,l[1:])
#     else:
#         return 0
middle_result = dict()
def calcM(total,l):
    if len(l) > 0 :
        if total < l[0]:
            return calcM(total,l[1:])
        if total == l[0]:
            return 1 + calcM(total,l[1:])
        return calcM(total - l[0],)+calcM(total,l[1:])
    else:
        return 0

def calcM1(total):  #total > 0
    # 结束状态
    if total < 0:
        return 0
    if total == 0:
        return 1
    if total in middle_result:
        return middle_result[total]
    # 开始状态
    result =  calcM1(total-1)+calcM1(total-2)+calcM1(total-3)
    middle_result[total]=result
    return result

print(calcM1(t))

    
