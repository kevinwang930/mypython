
# 数字颠倒 

int_str = input()
result = []
for x in int_str:
    result.insert(0,x)
str_result = ''.join(result)
print(str_result)



print(input()[::-1])