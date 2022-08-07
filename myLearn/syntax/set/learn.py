a = {1,2,3}
b = {1,2,4}
list_set = {(1,2),(1,3)}
print(a&b)
print(a|b)
print(a-b)
print(a^b)
list_set.add((1,4))
list_set.remove((1,2))
print(list_set)

set1 = {1,2,3}
set2 = set(set1)
set1.remove(1)
print(set2)