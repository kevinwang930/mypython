# 输入整型数组和排序标识，对其元素按照升序或降序进行排序 

qty_string = input()
qty = int(qty_string)
arr_str = input()
arr_num_string = arr_str.split(' ')
arr_num = []
for num_str in arr_num_string:
    arr_num.append(int(num_str))
sort_order = int(input())
if sort_order == 1:
    arr_num.sort(reverse=True)
else:
    arr_num.sort()
print(*arr_num,' ')