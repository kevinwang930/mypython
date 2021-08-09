# programming languages list
import sys
s = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
s.pop(0)
print(s)
s.pop(0)
print(s)
s1 = list(s)
print(s1)

c = set()
if c:
    print('empty set')
    
    
print(b'1' + b'2')
print(str(1))


a = ('a','b')
b = ['a','b']

b[0] ='b'
print(a[1])
print(b[1])


#scope and local

ai = 1

def local():
    ai = 2
    return ai


ai = local()
print(ai)


#class test

class myclass:
    ix = 123456
    
x = myclass()
x.counter = 1
del x.counter


#decode and encode

astr = 'kevin'
ab = astr.encode('utf-8')
ac = ab.decode('utf-8')
print(astr)
print(ab)
print(ac)

#local variable

def locala():
    a = []
    a.append('test')
    return a    
print(locala())

#input
# datai = input()
# print(datai)

#f string
username = 'kevin'.encode('utf-8')
HEADER_LENGTH = 10
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
print(f"{HEADER_LENGTH}")
print(f"{11:<10}")
print("My name is {0[name]}".format(dict(name='Fred')))
print("My name is {0:3}".format('Fred','kevin'))
print(len(username_header))
print(username_header)
print(username_header + username)
# print(a)

#int size

ints = bin(1)
print(ints)

#pyqt test
# from PyQt5.QtWidgets import QDialog,QApplication
# class frame(QDialog):
#     def __init__(self):
#         super().__init__()
#         print('frame initial')
        

# app = QApplication([])
# window = frame()

# window.show()
# app.exec_()
print(sys.getsizeof('a'.encode('utf-8')))

#test class method with parenthsis
class testclass():
    def testprint(self):
        print('testclass.testprint')
        
testa = testclass()
print(testa.testprint)

#boolean and if
if None:
    print('none')
else:
    print('yes')