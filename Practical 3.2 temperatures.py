MENU_1 = "C - Convert Celsius to Fahrenheit"
MENU_2 = "F - Convert Fahrenheit to Celsius"
MENU_3 = "Q - Quit"


def main():
    """Celsius and fahrenheit converting"""
    print("%s\n" \
          "%s\n" \
          "%s\n" % (MENU_1, MENU_2, MENU_3))
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)

main()