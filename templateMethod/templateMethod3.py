from abc import ABC, abstractmethod

#other hooks can be added if necessary

class Travel(ABC):
    @abstractmethod
    def outward_journey(self):
        pass
    
    @abstractmethod
    def day1(self):
        pass
    
    @abstractmethod
    def day2(self):
        pass
    
    @abstractmethod
    def day3(self):
        pass
    
    @abstractmethod
    def return_journey(self):
        pass
    
    #template method - hook
    def itinerary(self):
        self.outward_journey()
        self.day1()
        self.day2()
        self.day3()
        self.return_journey()
        
class VeniceTrip(Travel):
    def outward_journey(self):
        print('Plane taking off...')
        
    def day1(self):
        print('Visit to Sait Marcus Church.')
    
    def day2(self):
        print('Visit to the Doge Palace.')

    def day3(self):
        print('Enjoy the food next to Rialto Bridge.')
    
    def return_journey(self):
        print('Plane taking off...')
        
class MalvinasTrip(Travel):
    def outward_journey(self):
        print('Bus trip...')
        
    def day1(self):
        print('Enjoy marine life by boat.')
    
    def day2(self):
        print('Practice water sports.')

    def day3(self):
        print('Relax on the beach and enjoy the sunny day.')
    
    def return_journey(self):
        print('Bus trip...')
        
class TravelAngency:
    def prepare_trip(self):
        option = input('Which place would you like to visit? [Venice, Malvinas] ')
        if option == 'Venice':
            venice = VeniceTrip()
            venice.itinerary()
        elif option == 'Malvinas':
            malvinas = MalvinasTrip()
            malvinas.itinerary()
        else:
            print('Invalid destination.')
            
agency = TravelAngency()
agency.prepare_trip()