class Actor:
    def __init__(self):
        self.is_busy = False
    
    def unavailable(self):
        self.is_busy = True
        print(f'{type(self).__name__} is busy')
        
    def available(self):
        self.is_busy = False
        print(f'{type(self).__name__} is free')
        
    def check_availability(self):
        return self.is_busy
    
# Proxy
class Agent:
    def work(self):
        actor = Actor()
        if actor.check_availability():
            actor.unavailable()
        else:
            actor.available()

# Client
if __name__ == '__main__':
    agent = Agent()
    agent.work()