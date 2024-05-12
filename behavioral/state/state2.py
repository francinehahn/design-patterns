from abc import ABC

class ComputerState(ABC):
    name = 'ComputerState'
    allowed = []

    def change(self, state):
        if state.name in self.allowed:
            print(f'Current: {self} => alterado para um novo estado: {state.name}')
            self.__class__ = state
        else:
            print(f'Current: {self} => não é possível mudar para o {state.name}')

    def __str__(self):
        return self.name

class TurnOn(ComputerState):
    name = 'TurnOn'
    allowed = ['TurnOff', 'Suspend', 'Hibernate']
    
class TurnOff(ComputerState):
    name = 'TurnOff'
    allowed = ['TurnOn']
    
class Suspend(ComputerState):
    name = 'Suspend'
    allowed = ['TurnOn']
    
class Hibernate(ComputerState):
    name = 'Hibernate'
    allowed = ['TurnOn']

# context
class Computer:
    def __init__(self, model = 'Dell'):
        self.model = model
        self.state = TurnOff()

    def change(self, state):
        self.state.change(state)
        
if __name__ == '__main__':
    computer = Computer()

    #Turn the computer on
    computer.change(TurnOn)

    #Turn the computer off
    computer.change(TurnOff)

    #Turn the computer on
    computer.change(TurnOn)

    #Suspend
    computer.change(Suspend)

    #Hibernate
    computer.change(Hibernate)

    #Turn the computer on
    computer.change(TurnOn)

    #Hibernate
    computer.change(Hibernate)