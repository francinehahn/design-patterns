from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def talk(self):
        pass
    
class Dog(Animal):
    def talk(self):
        print('Au Au!')
        
class Cat(Animal):
    def talk(self):
        print('Miau!')
        
class Factory:
    def create_animal(self, animal_type:str):
        return eval(animal_type)().talk()
    
# simulate a client
if __name__ == '__main__':
    factory = Factory()
    animal = input('Which animal do you want to create? [Dog, Cat] ')
    factory.create_animal(animal)
    