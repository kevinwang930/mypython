
def judgePoint24(cards):
    if len(cards) == 1:
        return abs(cards[0]-24) < 0.000001
    
    for i in range(len(cards)-1):
        for j in range(i+1,len(cards)):
            rst = cards[:i]+ cards[i+1:j] + cards[j+1:] 
            x = cards[i]
            y = cards[j]
            if judgePoint24(rst + [x+y]):
                return True
            if judgePoint24(rst+[x-y]):
                return True
            if judgePoint24(rst + [y-x]):
                return True
            if judgePoint24(rst + [x*y]):
                return True
            if  y > 0 and judgePoint24(rst+[x/y]):
                return True
            if x > 0 and judgePoint24(rst+[y/x]):
                return True
    return False
            

while True:
    try:
        cards = [int(i) for i in input().split()]
        print(str(judgePoint24(cards)).lower())
    except:
        break