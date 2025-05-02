import unittest
from services.energy_service import get_daily_building_consumption

class TestEnergy(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(get_daily_building_consumption(1, '2023-10-01'), 150.2)

if __name__ == '__main__':
    unittest.main()
