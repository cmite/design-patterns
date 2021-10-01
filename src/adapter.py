class Target:
    """Desired interface for client."""

    def request(self) -> dict:
        """Request something."""
        return {"response": "this is a response message"}


class Adaptee:
    """Class to be adapted for client."""

    def specific_request(self) -> str:
        """Request something."""
        return "this is a specific response"


class Adapter(Adaptee, Target):
    """Class to adapt Adaptee to Target."""

    def request(self) -> dict:
        """Adapter for specific_request."""
        return {"response": self.specific_request()}


if __name__ == "__main__":
    adapter = Adapter()
    print(adapter.request())
