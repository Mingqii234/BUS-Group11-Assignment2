import random
from datetime import datetime, timedelta
import pandas as pd


class Dormitory(Building):
    def __init__(self, building_id):
        super().__init__(building_id)

class Laboratory(Building):
    def __init__(self, building_id):
        super().__init__(building_id)

class Classroom(Building):
    def __init__(self, building_id):
        super().__init__(building_id)


class EnergySystem:
    def __init__(self, building_ids=None, device_types=None):
        self.building_ids = building_ids or ["B001", "B002"]
        self.device_types = device_types or ["AC", "Heater", "Light", "Computer"]
        self.buildings = []

    def simulate_data(self, num_days=7, start_date=None, hour_range=(8, 18)):
        start_date = start_date or datetime.now()
        start_date = start_date.replace(minute=0, second=0, microsecond=0)

        for bid in self.building_ids:
            if "Dorm" in bid:
                building = Dormitory(bid)
            elif "Lab" in bid or "Laboratory" in bid:
                building = Laboratory(bid)
            elif "Classroom" in bid:
                building = Classroom(bid)
            else:
                building = Building(bid)

            for dname in self.device_types:
                dev = Device(dname, bid)
                for day_offset in range(num_days):
                    current_date = (start_date - timedelta(days=day_offset)).date()
                    random_hour = random.randint(hour_range[0], hour_range[1])
                    random_minute = random.randint(0, 59)
                    random_second = random.randint(0, 59)
                    current_datetime = datetime.combine(current_date, datetime.min.time()).replace(hour=random_hour, minute=random_minute, second=random_second)

                    energy = round(random.uniform(0.5, 5.5), 2)
                    dev.add_usage(current_datetime, energy)
                building.add_device(dev)
            self.buildings.append(building)

    def export_to_csv(self, filename="energy_report.csv"):
        records = []
        for b in self.buildings:
            for d in b.get_devices():
                for ts, en in d.get_usage_by_day():
                    records.append({
                        "Building_ID": b.id,
                        "Device": d.name,
                        "Datetime": ts.strftime("%Y-%m-%d %H:%M:%S"),
                        "Energy(kWh)": en
                    })
        df = pd.DataFrame(records, columns=["Building_ID", "Device", "Datetime", "Energy(kWh)"])
        if df.empty:
            df = pd.DataFrame(columns=["Building_ID", "Device", "Datetime", "Energy(kWh)"])
        df.to_csv(filename, index=False)