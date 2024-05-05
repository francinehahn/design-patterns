class University(type):
    def __call__(cls, *args, **kwargs):
        print(f'------These are the arguments: {args}')
        return type.__call__(cls, *args, **kwargs)
    
class Geek(metaclass=University):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

obj = Geek(42, 23)
print(obj)