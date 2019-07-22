"""
Version.

Holds version information.
Attributes:
 - major
 - minor
 - patch


properties:
 - version
"""


class Version:
    """Version."""

    major = 0
    minor = 0
    patch = 0

    @property
    def version(self):
        """Return set version as a string."""
        return f"{self.major}.{self.minor}.{self.patch}"
