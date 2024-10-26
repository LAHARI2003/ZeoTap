import unittest
from weather_monitor import kelvin_to_celsius

class TestWeatherMonitor(unittest.TestCase):

    def test_kelvin_to_celsius(self):
        self.assertEqual(kelvin_to_celsius(300), 26.85)

if __name__ == "__main__":
    unittest.main()
