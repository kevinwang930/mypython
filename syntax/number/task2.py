# 求int型正整数在内存中存储时1的个数 

def function_a():
    string_a = input()
    int_a = int(string_a)
    bin_a = bin(int_a)
    # sbin_a = str(bin_a)
    qty_1 = 0
    for s in bin_a[2:]:
        if int(s) == 1:
            qty_1 +=1
    print(qty_1)


function_a()