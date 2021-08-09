from import_package import test2
test2.secondtest()


import import_package.test3 as test3
test3.thirdtest()
from import_package.test3 import thirdtest 
thirdtest()