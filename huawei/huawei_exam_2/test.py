a = 129
b = bin(a).zfill(8)
print(b)
print(len(b))

c = int('110',2)
print(c)


d = int('011',2)
f = int('100',2)
e = d|f
print(e)


l = [[1,2],[2,3]]
if [1,2] in l:
    print(True)