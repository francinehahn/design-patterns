from abc import ABC, abstractmethod

# Command
class Order(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Command
class PurchaseOrder(Order):
    def __init__(self, share):
        self.share = share

    def execute(self):
        self.share.purchase()

# Concrete Command
class SalesOrder(Order):
    def __init__(self, share):
        self.share = share

    def execute(self):
        self.share.sell()

# Receiver
class Share:
    def purchase(self):
        print('You will purchase shares!')
    def sell(self):
        print('You will sell shares!')

# Invoker
class Agent:
    def __init__(self):
        self.__orders_queue = []
        
    def add_to_orders_queue(self, order):
        self.__orders_queue.append(order)
        order.execute()
        
if __name__ == '__main__':
    share = Share()
    purchase_order = PurchaseOrder(share=share)
    sales_order = SalesOrder(share=share)
    
    agent = Agent()
    agent.add_to_orders_queue(purchase_order)
    agent.add_to_orders_queue(sales_order)
