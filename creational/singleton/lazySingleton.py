class LazySingleton(object):
    __instance = None
    
    def __init__(self):
        # new method is executed before init method
        if not LazySingleton.__instance:
            print('__init__ method has been called...')
        else:
            print(f'The instance has already been created: {self.get_instance()}')
    
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance
        

s1 = LazySingleton()
print(f'Object created now: {s1.get_instance()}')

s2 = LazySingleton()