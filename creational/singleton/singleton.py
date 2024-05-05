class Singleton(object):
    def __new__(cls):
        # new method is executed before init method
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'Creating the object {cls.instance}')
        return cls.instance

s1 = Singleton()
print(f'Instance 1: {id(s1)}')

s2 = Singleton()
print(f'Instance 1: {id(s2)}')