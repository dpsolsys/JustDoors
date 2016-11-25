 import unittest

class GeoThing:

    def __init__(self, states, cities):
        self.states = states
        self.cities = cities

    def get_state_abbreviation(self, state):
        return self.states[state]

    def list_cities_for_state(self, state):
        return self.cities[state]

class TestGeoThing(unittest.TestCase):

    def test_state_abbreviations(self):
        states = { "FooState": "FOO" }
        cities = {}

        sut = GeoThing(states, cities)
        abbreviation = sut.get_state_abbreviation("FooState")
        self.assertEqual(abbreviation, "FOO")

    def test_list_cities_returns_list(self):
        states = {}
        cities = {
            "CA": ["San Francisco", "Los Angelas"],
        }

        sut = GeoThing(states, cities)
        city_list  = sut.list_cities_for_state("CA")
        self.assertEqual(city_list.index("San Francisco"), 0)
        self.assertEqual(city_list.index("Los Angelas"), 1)

class Progam:

    def __init__(self):
        Pass


    def run():
        cities = {} # Populate Cities here from a Json file or db
        states = {} # Populate States here from a Json file or db
        geo = GeoThing(cities, states)

        # ... Rest of code goes here.

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGeoThing)

    unittest.TextTestRunner(verbosity=2).run(suite)

    #  Exaample of production app
    #program = Program()
    #program.run()
