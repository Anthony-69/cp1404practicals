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


def run_tests():
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    c = ProgrammingLanguage("C++", "Static", False, 1983)
    # c is the programming language C++
    # THe "++" is not added due to it causing errors
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    languages = [java, c, python, visual_basic, ruby]
    for language in languages:
        print(language)
    print("The dynamically typed languages include:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
