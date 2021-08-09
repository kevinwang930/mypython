class person(type):
    # def __init__(self):
    #     print('this is person class')
    #     print(self.__dict__)

    def __new__(cls, name, base, namespace, *args, **kwargs):
        print(f'namespace is {namespace}')

        return type.__new__(cls, name, base, namespace)

    @classmethod
    def __prepare__(name, bases, *args, **kwargs):
        dict1 = {}
        dict1['a'] = 1
        return dict1


class teacher(metaclass=person):

    def __init_subclass__(cls,  **kwargs):
        super().__init_subclass__(**kwargs)
        print('begin initilize subclass')
        print(kwargs)
        # cls.default_name = default_name




class teacherwdname(teacher, default_name='kevin'):
    teach = 'physics'


c = teacherwdname()


print(c.teach)
print(teacherwdname.__dict__)


    


