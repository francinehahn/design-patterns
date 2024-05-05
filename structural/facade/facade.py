# Facade
class EventManagement:
    def __init__(self):
        print('Event Management: I will manage everything!')
        
    def organize(self):
        self.party_room = PartyRoom()
        self.party_room.schedule()
        
        self.florist = Florist()
        self.florist.arrange_flowers()
        
        self.restaurant = Restaurant()
        self.restaurant.prepare()
        
        self.band = Band()
        self.band.set_up_stage()
        

class PartyRoom:
    def __init__(self):
        print('Party room: Space for all types of events...')
        
    def _is_available(self):
        print('Party room: Is this space available?\n')
        return True
        
    def schedule(self):
        if self._is_available():
            print('Party room was successfully scheduled!\n')
            
class Florist:
    def __init__(self):
        print('Florist: All types of flowers...')

    def arrange_flowers(self):
        print('Florist: tulips, roses and lilies will be used!\n')
        
class Restaurant:
    def __init__(self):
        print('Restaurant: Food for events...')
        
    def prepare(self):
        print('Restaurant: Brazilian and italian food will be served.\n')
        
class Band:
    def __init__(self):
        print('Band: Music for events...')
        
    def set_up_stage(self):
        print('Stage is ready!\n')
        
# Cliente
class Client:
    def __init__(self):
        print('Client: Uauu! Preparing for the weading!')
        
    def hire_manager(self):
        print('Client: I will hire a manager to organize the weading.\n')
    
        em = EventManagement()
        em.organize()
    
    def __del__(self):
        print('It was very easy to organize this event!\n')
        
if __name__ == '__main__':
    client = Client()
    client.hire_manager()