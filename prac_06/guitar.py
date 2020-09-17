"""
CP1404 Practical
Guitar class
"""
CURRENT_YEAR = 2020
VINTAGE_AGE = 50


class Guitar:
    """Class for guitar data."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Format the data of a guitar."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the guitars age"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Calculate if the guitar is a vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Sort guitar based on released year."""
        return self.year < other.year
