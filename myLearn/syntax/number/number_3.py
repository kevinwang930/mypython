a, b = map(int, input().split())
  
def gcf(x,y):
    if x>y:
        greater = x
    else:
        greater = y
    while y!=0:
        x,y=y,x%y
    return x
 
print(int(a*b/gcf(a,b)))