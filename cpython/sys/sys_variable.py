import sys
print(sys.builtin_module_names)
print(sys.int_info)
print(sys.path)
print(sys.path_hooks)
print(sys.base_prefix)
print(sys.prefix)
print(type(sys))
print(sys.modules)

print(type(__name__))
print(sys.modules['__main__'])
print(sys.path_hooks)
print(sys.modules['__main__'].__dict__)