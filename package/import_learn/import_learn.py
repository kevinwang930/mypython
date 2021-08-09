from import_package import test2

from import_package.test3 import thirdtest

test2.secondtest()
thirdtest()

from import_package import variable
print(variable.a)
variable.test_a()

print(variable.a)