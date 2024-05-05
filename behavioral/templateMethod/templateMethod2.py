from abc import ABC, abstractmethod

#other hooks can be added if necessary

class AbstractClass(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def operation1(self):
        pass
    
    @abstractmethod
    def operation2(self):
        pass
    
    def template_method(self):
        print('Defining the algorithm...')
        self.operation1()
        self.operation2()
        
class ConcreteClass(AbstractClass):
    def operation1(self):
        print('Concrete operation 1')
        
    def operation2(self):
        print('Concrete operation 2')
        
class Client:
    def main(self):
        self.concrete = ConcreteClass()
        self.concrete.template_method()
        
client = Client()
client.main()