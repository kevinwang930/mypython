import importlib
import sys
def test():
    package = importlib.import_module("import_package")
    # print(sys.modules)
    print(package.a)
    print('after import')

print('before import')
test()
# print("outside import func ",sys.modules)
package = sys.modules['import_package']
print(package.a)
