# HJ58 输入n个整数，输出其中最小的k个 


while True:
    try:
        n,k = [int(i) for i in input().split()]
        l1 = [int(i) for i in input().split()]
        l2 = [l1[0]]
        for i in range(1,len(l1)):
            inserted = 0
            for j in range(len(l2)):
                if l1[i]<l2[j]:
                    l2.insert(j,l1[i])
                    inserted = 1
                    break
            if not inserted:
                l2.append(l1[i])

        print(*l2[:k])
    except:
        break