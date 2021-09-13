class MyIterator():
    def __init__(self):
        self.list = []
        self.position = 0

    def add_name(self,name):
        self.list.append(name)

    def __iter__(self):
        return self  # 返回一个迭代器

    def __next__(self):
        if self.position < len(self.list):
            item = self.list[self.position]
            self.position += 1
            return item
        else:
            raise StopIteration


people = MyIterator()  # people对象既是一个迭代器，也是一个可迭代对象
people.add_name("张三")
people.add_name("李四")
people.add_name("王五")

# 把people当做一个迭代器来看时
print(next(people))
print(next(people))
print(next(people))

# 把humen当做一个可迭代对象来看时
humen = MyIterator()  # 因为迭代器只能用一次，再用会抛出错误，所以需要再创建
humen.add_name("张三")
humen.add_name("李四")
humen.add_name("王五")
iterator = iter(humen)  # iter()方法获取可迭代对象的迭代器
print(next(iterator))
print(next(iterator))
print(next(iterator))