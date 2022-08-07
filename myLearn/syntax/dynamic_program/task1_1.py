# 王强今天很开心，公司发给N元的年终奖。王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的

main = []
acc = {}

amount,qty = [int(i) for i in input().split()]

amount //=10
for k in range(qty):
    v,w,q = [int(i) for i in input().split()]
    v //=10
    r = v*w
    if q == 0:
        main.append([v,r,k+1])
    elif q in acc.keys():
        acc[q].append([v,r])
    else:
        acc[q]=[[v,r]]

dt = [[0]*(amount+1) for _ in range(qty+1)]
def calc():
    for i in range(1,len(main)+1): # main count
        v,r,n = main[i-1]
        for j in range(1,amount+1): # total amount count
            if j >= v:
                if n in acc.keys():
                    max_i = dt[i-1][j-v]+r
                    v_accu = v
                    r_accu = r
                    for v_item,r_item in acc[n]:
                        j_a = j-v-v_item
                        r_a = r+r_item
                        v_accu +=v_item
                        r_accu += r_item
                        if j_a >= 0:
                            max_i = max(max_i,dt[i-1][j_a]+r_a)
                    if j-v_accu >=0:
                        max_i = max(max_i,dt[i-1][j-v_accu]+r_accu)
                    dt[i][j] = max(dt[i-1][j],max_i)
                else:
                    dt[i][j] = max(dt[i-1][j],dt[i-1][j-v]+r)
            else:
                dt[i][j] = dt[i-1][j]
    return dt[len(main)][amount]

# print(main,acc)
print(calc()*10)
