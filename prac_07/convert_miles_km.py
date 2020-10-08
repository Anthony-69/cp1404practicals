from kivy.app import App
from kivy.lang import Builder


MILES_TO_KM = 1.60934


class MilesToKilos(App):
    """This is an app to convert miles to kilometres"""
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def determine_conversion(self):
        """Converts given value or incremented value to kilometres"""
        value = self.validate_input()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def UpOrDown(self, change):
        """Adds or subtracts 1 from the value when the respective Up/Down button is clicked"""
        value = self.validate_input() + change
        self.root.ids.input_miles.text = str(value)
        self.determine_conversion()

    def validate_input(self):
        """Makes sure input is an integer"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilos().run()