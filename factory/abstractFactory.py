from abc import ABC, abstractmethod

# Abstract Factory
class PizzaFactory(ABC):
    @abstractmethod
    def create_vegan_pizza(self):
        pass
    
    @abstractmethod
    def create_non_vegan_pizza(self):
        pass
    
# Concrete Factory A
class BrazilianPizza(PizzaFactory):
    def create_vegan_pizza(self):
        return MandiocaPizza()
    
    def create_non_vegan_pizza(self):
        return ShrimpPizza()
    
# Concrete Factory B
class ItalianPizza(PizzaFactory):
    def create_vegan_pizza(self):
        return BroccoliPizza()
    
    def create_non_vegan_pizza(self):
        return BolognaPizza()
    

# Abstract Product A
class VeganPizza(ABC):
    @abstractmethod
    def prepare(self, vegan_pizza):
        pass
    
# Abstract product B
class NonVeganPizza(ABC):
    @abstractmethod
    def serve(self, vegan_pizza):
        pass
    
# Concrete Porduct
class MandiocaPizza(VeganPizza):
    def prepare(self, vegan_pizza):
        print(f'Making {type(self).__name__}')
        
# Concrete Porduct
class ShrimpPizza(NonVeganPizza):
    def serve(self, vegan_pizza):
        print(f'{type(self).__name__} is served with shrimp on top of {type(vegan_pizza).__name__}')

# Concrete Porduct
class BroccoliPizza(VeganPizza):
    def prepare(self, vegan_pizza):
        print(f'Making {type(self).__name__}')

# Concrete Porduct
class BolognaPizza(NonVeganPizza):
    def serve(self, vegan_pizza):
        print(f'{type(self).__name__} is served with meat on top of {type(vegan_pizza).__name__}')
        

# client
class Pizzaria:
    def make_pizzas(self):
        for factory in [BrazilianPizza(), ItalianPizza()]:
            self.factory = factory
            self.non_vegan_pizza = self.factory.create_non_vegan_pizza()
            self.vegan_pizza = self.factory.create_vegan_pizza()
            self.vegan_pizza.prepare(self.vegan_pizza)
            self.non_vegan_pizza.serve(self.vegan_pizza)

pizzaria = Pizzaria()
pizzaria.make_pizzas()