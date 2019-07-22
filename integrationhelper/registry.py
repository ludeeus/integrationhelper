"""Registry."""


class Registry:
    """Registry."""

    register = {}

    def add(self, key, value):
        """Add to the Registry."""
        self.register[key] = value

    def remove(self, key):
        """Remove from Registry."""
        if key in self.register:
            del self.register[key]
