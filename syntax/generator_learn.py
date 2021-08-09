import dis
def example():
    lst = (1,2,3,4)
    for i in lst:
        yield i

gen = example()
print(gen.__next__())
print(gen.__next__())

print(gen.gi_code.co_name)
print(gen.__next__)
print(dir(gen))
# print(gen.gen_memberlist)
# dis.disco(gen.gi_code)



