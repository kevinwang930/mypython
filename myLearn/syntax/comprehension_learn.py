
a_list = [1, '4', 9, 'a', 0, 4]

squared_ints = [ e**2 for e in a_list if isinstance(e,int) ]

print(squared_ints)

#dict comprehension
input_list = [1, 2, 3, 4, 5, 6, 7]

dict_using_comp = {var: var ** 3 for var in input_list if var % 2 != 0}

print("Output Dictionary using dictionary comprehensions:",
      dict_using_comp)

dict1 = {'a':1,'b':2}
dict2 = {key:value**2 for (key,value) in dict1.items()}
print(dict2)
