import random


def main():
    """Get score and return grade."""
    score = float(input("Enter score: "))
    while 0 <= score >= 101:
        print("Invalid score")
        score = float(input("Enter score: "))
    else:
        print(determine_response(score))
    number = random.randint(0, 100)
    print(number)


def determine_response(score):
    """Determine the status of score."""
    if 100 >= score >= 90:
        return"Excellent"
    elif 89 >= score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
