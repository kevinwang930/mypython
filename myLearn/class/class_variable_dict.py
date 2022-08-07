class base:
    dict = {'name':"kevin"}

a = base()
print(a.dict['name'])
a.dict['name'] = 'wang'

b = base()
print(a.dict['name'])