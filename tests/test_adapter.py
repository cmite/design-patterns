from src.adapter import Adapter


class TestAdapter:
    """Class to test Adapter."""

    def test_request(self):
        """Test the request method."""
        adapter = Adapter()
        expected = {"response": "this is a specific response"}
        assert expected == adapter.request()
