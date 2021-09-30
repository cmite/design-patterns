from src.observer import TemperatureSubscriber
from src.observer import PressureSubscriber
from src.observer import HumiditySubscriber
from src.observer import Publisher


class TestTemperatureSubscriber:
    """Class to test TemperatureSubscriber."""

    def test_update(self):
        """Test the update method."""
        subscriber = TemperatureSubscriber()
        context = {"temperature": 20}
        expected = "Current temperature is 20°C"
        assert expected == subscriber.update(context)


class TestPressureSubscriber:
    """Class to test PressureSubscriber."""

    def test_update(self):
        """Test the update method."""
        subscriber = PressureSubscriber()
        context = {"pressure": 0.23}
        expected = "Current pressure is 0.23 atm"
        assert expected == subscriber.update(context)


class TestHumiditySubscriber:
    """Class to test HumiditySubscriber."""

    def test_update(self):
        """Test the update method."""
        subscriber = HumiditySubscriber()
        context = {"humidity": 57}
        expected = "Current humidity level is 57%"
        assert expected == subscriber.update(context)


class TestPublisher:
    """Class to test Publisher."""

    def test_subscribe(self, mocker):
        """Test the subscribe method."""
        publisher = Publisher()
        subscriber = mocker.Mock()
        publisher.subscribe(subscriber)
        assert [subscriber] == publisher.subscribers

    def test_multiple_subscribe(self, mocker):
        """Test the subscribe method multiple times."""
        publisher = Publisher()
        subscriber = mocker.Mock()
        publisher.subscribe(subscriber)
        publisher.subscribe(subscriber)
        assert [subscriber] == publisher.subscribers

    def test_unsubscribe(self, mocker):
        """Test the unsubscribe method."""
        publisher = Publisher()
        subscriber = mocker.Mock()
        publisher.subscribe(subscriber)
        publisher.unsubscribe(subscriber)
        assert [] == publisher.subscribers

    def test_multiple_unsubscribe(self, mocker):
        """Test the unsubscribe method multiple times."""
        publisher = Publisher()
        subscriber = mocker.Mock()
        publisher.subscribe(subscriber)
        publisher.unsubscribe(subscriber)
        publisher.unsubscribe(subscriber)
        assert [] == publisher.subscribers

    def test_notify_subscribers(self, mocker):
        """Test the notify_subscribers method."""
        publisher = Publisher()
        context = {"temperature": 10, "pressure": 0.32, "humidity": 40}
        publisher.context = context
        first_subscriber = mocker.Mock()
        second_subscriber = mocker.Mock()
        publisher.subscribe(first_subscriber)
        publisher.subscribe(second_subscriber)
        publisher.notify_subscribers()
        first_subscriber.update.assert_called_once_with(context)
        second_subscriber.update.assert_called_once_with(context)

    def test_process(self, mocker):
        """Test the process method."""
        publisher = Publisher()
        first_subscriber = mocker.Mock()
        second_subscriber = mocker.Mock()
        publisher.subscribe(first_subscriber)
        publisher.subscribe(second_subscriber)
        publisher.process()
        first_subscriber.update.assert_called_once()
        second_subscriber.update.assert_called_once()
