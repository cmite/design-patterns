from src.singleton import Singleton


class TestSingleton:

    def test_singleton(self):
        """Test two singleton instances are the same."""
        first_singleton = Singleton()
        second_singleton = Singleton()

        assert first_singleton == second_singleton