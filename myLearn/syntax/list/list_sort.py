list1 = [['1230', 'a'], ['1230', 'b'], ['1234', 'c']]
list1.sort(key=lambda x: (x[0], ord('z') - ord(x[1])), reverse=True)
print(list1)
