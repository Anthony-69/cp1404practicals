"""
CP1404/CP5632 Practical
"""


class ProgrammingLanguage:
    """Show the information about different languages."""

    def __init__(self, name, typing, reflection, first_year_appeared):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.first_year_appeared = first_year_appeared

    def __str__(self):
        """Format data neatly."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing, self.reflection, self.first_year_appeared)

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"