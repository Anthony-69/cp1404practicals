"""
CP1404 Practical
Word occurrences
Student: Anthony Bokor
"""

phrase_to_count = {}
text = input("Text: ")
phrases = text.split()
# Finds how often a letter occurs
for phrase in phrases:
    recurrence = phrase_to_count.get(phrase, 0)
    phrase_to_count[phrase] = recurrence + 1
phrase = list(phrase_to_count.keys())
phrase.sort()
# Uses the max length of a word to find the width of the output
max_length = max((len(phrase) for phrase in phrases))
for phrase in phrases:
    print("{:{}} : {}".format(phrase, max_length, phrase_to_count[phrase]))