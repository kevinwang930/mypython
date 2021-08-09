import dis
import marshal
import py_compile
co =py_compile.compile('generator.py')
# print(co.co_code)
# dis.dis(co.co_code)
with open(co, 'rb') as f:
    code = f.read()
    c = marshal.loads(code[16:])
    dis.dis(c.co_code)
    dis.show_code(c)

print('co_names is ',c.co_names) 
print('co_consts are ',c.co_consts)

print(c.co_consts[0].co_consts)