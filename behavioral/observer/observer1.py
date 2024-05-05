class Object:
    def __init__(self):
        self.__observers = []

    def __repr__(self):
        return '::Object::'

    def register(self, observer):
        self.__observers.append(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

class ObserverA:
    def __init__(self, object):
        object.register(self)

    def notify(self, object, *args):
        print(f'The {type(self).__name__} has received a {args[0]} from {object}')

class ObserverB:
    def __init__(self, object):
        object.register(self)

    def notify(self, object, *args):
        print(f'The {type(self).__name__} has received a {args[0]} from {object}')

obj = Object()
obsA = ObserverA(obj)
obsB = ObserverB(obj)
obj.notify_all('notification')