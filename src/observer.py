import random
from abc import ABC
from abc import abstractmethod


class Sensor(ABC):
    """Abstract Sensor class."""

    @classmethod
    @abstractmethod
    def get_data(cls):
        raise NotImplementedError


class Temperature(Sensor):
    """Temperator Data Sensor."""

    @classmethod
    def get_data(cls) -> int:
        return random.randint(0, 50)


class Pressure(Sensor):
    """Pressure Data Sensor."""

    @classmethod
    def get_data(cls) -> float:
        return round(random.random(), 2)


class Humidity(Sensor):
    """Humidity Data Sensor."""

    @classmethod
    def get_data(cls) -> int:
        return random.randint(0, 100)


class Subscriber(ABC):
    """Abstract class for subscribers."""

    @abstractmethod
    def update(self, context: dict):
        """Update display."""
        raise NotImplementedError


class TemperatureSubscriber(Subscriber):
    """Subscriber for temperature sensor."""

    def update(self, context: dict) -> str:
        temperature = context.get('temperature')
        return f"Current temperature is {temperature}°C"


class PressureSubscriber(Subscriber):
    """Subscriber for pressure sensor."""

    def update(self, context: dict) -> str:
        pressure = context.get('pressure')
        return f"Current pressure is {pressure} atm"


class HumiditySubscriber(Subscriber):
    """Subscriber for humidity sensor."""

    def update(self, context: dict) -> str:
        humidity = context.get('humidity')
        return f"Current humidity level is {humidity}%"


class Publisher:

    def __init__(self):
        self.subscribers = []
        self.context = {}

    def subscribe(self, subscriber: Subscriber):
        """Append a subscriber to the subscribers list."""
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        """Remove a subscriber from the subscribers list."""
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)
    
    def notify_subscribers(self):
        """Notify all subscribers."""
        for subscriber in self.subscribers:
            subscriber.update(self.context)

    def process(self):
        """Main publisher process."""
        context = {
            "temperature": Temperature.get_data(),
            "pressure": Pressure.get_data(),
            "humidity": Humidity.get_data()
        }

        if context != self.context:
            self.context = context
            self.notify_subscribers()


if __name__ == '__main__':
    publisher = Publisher()
    tmp = TemperatureSubscriber()
    psr = PressureSubscriber()
    hdt = HumiditySubscriber()
    publisher.subscribe(tmp)
    publisher.subscribe(psr)
    publisher.subscribe(hdt)

    for i in range(100):
        publisher.process()