# 有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，问第n个月的兔子总数为多少？ 


out = [1,1,1]


waterMark = 2
def iteration(n):
    global waterMark
    if n <= waterMark:
        return out[n]
    else:
        for i in range(waterMark+1,n+1):
            out.append(out[i-1] + out[i-2]) 
    waterMark = n
    return out[n]

while True:
    try:
        month = int(input())
        if month == 0:
            break
        print(iteration(month))
    except:
        break
        