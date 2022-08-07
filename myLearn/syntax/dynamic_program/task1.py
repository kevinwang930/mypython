main = []
acc = {}

amount,qty = map(int,input().split())
for i in range(qty):
    v,p,q = map(int,input().split())
    if q == 0:
        main.append([i+1,v,p,q])
    else:
        if q in acc.keys():
            acc[q].append([i+1,v,p,q])
        else:
            acc[q] = [[i+1,v,p,q]]
    
        

def f(m,amount):
    if len(m) == 0:
        return 0
    else: 
        return max(first_include(m,amount), f(m[1:],amount))
    

def first_include(c,amount):
    n,v,p,q = c[0]
    if amount >= v:
        next_c = c[1:]
        if q == 0 and n in acc.keys():
            next_c = acc[n] + next_c
            
        result = v*p + f(next_c,amount-v)
        return result
    else:
        return 0
print(f(main,amount))