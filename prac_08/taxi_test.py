"""
CP1404/CP5632 Practical
Taxi test
"""

from prac_08.taxi import Taxi

def test():
    new_taxi = Taxi("Prius 1", 100, Taxi.price_per_km)
    new_taxi.start_fare()
    new_taxi.drive(40)
    new_taxi.get_fare()
    print(new_taxi)
    new_taxi.start_fare()
    new_taxi.drive(100)
    new_taxi.get_fare()
    print(new_taxi)


test()