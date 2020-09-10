"""
CP1404 Practical
Hex colours
Student: Anthony Bokor
"""

COLOURS_AND_KEYS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                    "aquamarine1": "#7fffd4", "azure1": "#foffff",
                    "beige": "#f5f5dc", "black": "#000000",
                    "blue1": "#0000ff", "BlueViolet": "#8a2be2",
                    "brown": "#a52a2a", "burlywood": "#deb887",
                    "CadetBlue1": "#98f5ff", "chartreuse1": "#7fff00",
                    "chocolate": "#d2691e", "coral": "#ff7f50",
                    "cornsilk1": "#fff8dc"}

colour_name = input("Give us a colours name: ")
while colour_name != "":
    print("The special key for {} is {}".format(colour_name, COLOURS_AND_KEYS.get(colour_name)))
    colour_name = input("Enter a colour name: ")