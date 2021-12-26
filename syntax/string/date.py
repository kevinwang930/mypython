#  根据输入的日期，计算是这一年的第几天。
# 保证年份为4位数且日期合法。
# 进阶：时间复杂度：，空间复杂度：

days = [31,28,31,30,31,30,31,31,30,31,30,31]

year,month,day= map(int,input().split())

days_count = sum(days[:month-1]) + day

if month > 2 and year%4==0 and  (year%400 == 0 or year%100 != 0):
    days_count = days_count + 1
print(days_count)