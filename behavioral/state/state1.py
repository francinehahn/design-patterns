from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def manipulate(self):
        pass

class ConcreteStateA(State):
    def manipulate(self):
        print('Concrete State A')

class ConcreteStateB(State):
    def manipulate(self):
        print('Concrete State B')

class Context(State):
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def manipulate(self):
        self.state.manipulate()
        

context = Context()
state_a = ConcreteStateA()
state_b = ConcreteStateB()

context.set_state(state_a)
context.manipulate()

context.set_state(state_b)
context.manipulate()