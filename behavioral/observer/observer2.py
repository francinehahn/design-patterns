from abc import ABC, abstractmethod

# Subject / Topic
class NewsAgency(ABC):
    def __init__(self):
        self.__subscribers = []
        self.__last_news = None

    def subscribe(self, subscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber=None):
        if not subscriber:
            return self.__subscribers.pop()
        else:
            return self.__subscribers.remove(subscriber)

    def notify_all(self):
        for subscriber in self.__subscribers:
            subscriber.notify()

    def get_subscribers(self):
        return [type(value).__name__ for value in self.__subscribers]

    def add_news(self, news):
        self.__last_news = news

    def show_news(self):
        return f'Urgent! {self.__last_news}'

# Observer interface
class SubscriptionType(ABC):
    @abstractmethod
    def notify(self):
        pass

# Observer A
class SmsSubscribers(SubscriptionType):
    def __init__(self, agency_news):
        self.agency_news = agency_news
        self.agency_news.subscribe(self)

    def notify(self):
        print(f'{type(self).__name__}: {self.agency_news.show_news()}')

# Observer B
class EmailSubscribers(SubscriptionType):
    def __init__(self, agency_news):
        self.agency_news = agency_news
        self.agency_news.subscribe(self)

    def notify(self):
        print(f'{type(self).__name__} {self.agency_news.show_news()}')

# Observer N
class OtherSubscribers(SubscriptionType):
    def __init__(self, agency_news):
        self.agency_news = agency_news
        self.agency_news.subscribe(self)

    def notify(self):
        print(f'{type(self).__name__} {self.agency_news.show_news()}')

# Client
if __name__ == '__main__':
    agency_news = NewsAgency()
    SmsSubscribers(agency_news)
    EmailSubscribers(agency_news)
    OtherSubscribers(agency_news)

    print(f'Subscribers: {agency_news.get_subscribers()}')

    agency_news.add_news('New python course available!')
    agency_news.notify_all()

    print(f'Unsubscribe: {type(agency_news.unsubscribe()).__name__}')
    print(f'Subscribers: {agency_news.get_subscribers()}')

    agency_news.add_news('New javascript course available!')
    agency_news.notify_all()