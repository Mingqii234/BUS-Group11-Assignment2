import unittest
from services.energy_service import get_daily_building_consumption
from models.energy_consumption import EnergyConsumption

class TestBuildingEnergy(unittest.TestCase):
    def setUp(self):
        self.test_records = [
            EnergyConsumption(building_id=1, date='2023-10-01', consumption_kwh=100.2),
            EnergyConsumption(building_id=1, date='2023-10-01', consumption_kwh=50.0),
            EnergyConsumption(building_id=2, date='2023-10-01', consumption_kwh=80.5),
        ]

    def test_valid_building(self):
        result = get_daily_building_consumption(1, '2023-10-01', records=self.test_records)
        self.assertEqual(result, 150.2)

    def test_invalid_building(self):
        try:
            get_daily_building_consumption(99, '2023-10-01', records=self.test_records)
            self.fail("Should have raised ValueError")
        except ValueError:
            pass


if __name__ == '__main__':
    unittest.main()

