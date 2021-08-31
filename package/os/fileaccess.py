import os
print(os.access(r'E:\git\myElectron\output\supplierReport_1.pdf',os.W_OK))
print(os.access(r'E:\git\myElectron\output\08.xlsx',os.W_OK))

try:
    with open(r'E:\git\myElectron\output\08.xlsx','W') as fd:
        pass
except:
    print('open blocked file failed')