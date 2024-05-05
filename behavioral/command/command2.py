from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, recv):
        self.recv = recv

    @abstractmethod
    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        self.recv.action()

class Receiver:
    def action(self):
        print('Receiver action!')

class Invoker:
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


if __name__ == '__main__':
    receiver = Receiver()
    cmd = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.command(cmd=cmd)
    invoker.execute()