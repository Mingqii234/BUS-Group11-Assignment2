import unittest
from models.building import Device
from models.energy_system import EnergySystem
from datetime import datetime, timedelta
import os
import pandas as pd


class TestEnergySystem(unittest.TestCase):

    def test_add_usage_positive(self):
        d = Device("AC", "B001")
        d.add_usage(datetime.now(), 3.5)
        self.assertEqual(len(d.usage_log), 1)

    def test_add_usage_negative(self):
        d = Device("Heater", "B001")
        with self.assertRaises(ValueError):
            d.add_usage(datetime.now(), -5)

    def test_total_energy_positive(self):
        d = Device("Light", "B001")
        d.add_usage(datetime.now(), 2.0)
        d.add_usage(datetime.now(), 3.0)
        self.assertEqual(d.get_total_energy(), 5.0)

    def test_total_energy_negative(self):
        d = Device("Computer", "B001")
        self.assertEqual(d.get_total_energy(), 0)

    def test_alert_detection_positive(self):
        sys = EnergySystem()
        sys.simulate_data()
        d = sys.buildings[0].devices[0]
        today = datetime.now()
        d.usage_log = [(today - timedelta(days=i), 4.6) for i in range(3)]
        self.assertGreaterEqual(d.get_recent_high_usage_days(), 3)

    def test_alert_detection_negative(self):
        d = Device("AC", "B001")
        for i in range(3):
            d.add_usage(datetime.now() - timedelta(days=i), 2.0)
        self.assertEqual(d.get_recent_high_usage_days(), 0)

    def test_export_csv_positive(self):
        sys = EnergySystem()
        sys.simulate_data()
        filename = "test_energy_output.csv"
        sys.export_to_csv(filename)
        self.assertTrue(os.path.exists(filename))
        df = pd.read_csv(filename)
        self.assertFalse(df.empty)
        os.remove(filename)

    def test_export_csv_negative(self):
        sys = EnergySystem()
        filename = "test_empty_output.csv"
        sys.export_to_csv(filename)
        df = pd.read_csv(filename)
        self.assertTrue(df.empty or len(df.columns) == 4)
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()