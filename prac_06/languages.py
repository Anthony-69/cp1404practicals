"""
CP1404/CP5632 Practical
"""

from prac_06.programming_language import ProgrammingLanguage


def run_main():
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
    run_main()
