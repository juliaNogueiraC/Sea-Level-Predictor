import unittest
from main 

class TestSeaLevelRise(unittest.TestCase):
    def test_predict_sea_level_rise(self):
        # Test for predict_sea_level_rise function
        slope = 0.1
        intercept = 5
        self.assertEqual(main.predict_sea_level_rise(2050, slope, intercept), 5.1)
        self.assertEqual(main.predict_sea_level_rise(2100, slope, intercept), 15)

if __name__ == "__main__":
    unittest.main()
