"""
Guitar
"""


class Guitar:
    """Represents a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self, current_year=2025):
        """Calculate the age of the guitar in years."""
        return current_year - self.year

    def is_vintage(self, current_year=2025):
        """Determine if the guitar is vintage."""
        return self.get_age(current_year) > 50

    def __lt__(self, other):
        """Determine of one guitar is less than the other based on year."""
        return self.year < other.year

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:1,.2f}"
