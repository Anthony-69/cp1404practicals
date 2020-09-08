"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subjects(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data


def display_subjects(data):
    for subject_data in data:
        print("{} is taught by {:12} and has {:3} students".format(*subject_data))


main()
