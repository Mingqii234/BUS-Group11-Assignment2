import random
from datetime import datetime, timedelta
import pandas as pd


class Device:
    def __init__(self, name, building_id):
        self.name = name
        self.building_id = building_id
        self.usage_log = [] # List of (date, energy) tuples for tracking daily usage

    def add_usage(self, timestamp, energy):
        self.usage_log.append((timestamp, energy)) # Add new (date, energy) entry

    def get_total_energy(self):
        return sum(e for _, e in self.usage_log) # Sum all energy values

    def get_recent_high_usage_days(self, threshold=4.5, days=3):
        count = 0
        # Sort the log by date, take the last `days` records
        for timestamp, energy in sorted(self.usage_log)[-days:]:
            if energy > threshold:
                count += 1
        return count

    def get_usage_by_day(self):
        return sorted(self.usage_log)



#Manages all buildings and simulation logic
class EnergySystem:
    def __init__(self, building_ids=None, device_types=None):
        self.building_ids = building_ids or ["B001", "B002"]
        self.device_types = device_types or ["AC", "Heater", "Light", "Computer"]
        self.buildings = []

    def simulate_data(self, num_days=7):
        for bid in self.building_ids:
            building = Building(bid) # Create a new building
            for dname in self.device_types:
                dev = Device(dname, bid) # Create a new device in this building
                for i in range(num_days):
                    date = datetime.now().date() - timedelta(days=i)
                    energy = round(random.uniform(0.5, 5.5), 2)  # Random energy value between 0.5 and 5.5
                    dev.add_usage(date, energy)
                building.add_device(dev)
            self.buildings.append(building)

#Export all device usage data into a CSV file
    def export_to_csv(self, filename="energy_report.csv"):
        records = []
        for b in self.buildings:
            for d in b.get_devices():
                for ts, en in d.get_usage_by_day():
                    records.append({
                        "Building_ID": b.id,
                        "Device": d.name,
                        "Date": ts,
                        "Energy(kWh)": en
                    })
        df = pd.DataFrame(records) # Pandas: Create DataFrame from the list of records
        if df.empty:
            df = pd.DataFrame(columns=["Building_ID", "Device", "Date", "Energy(kWh)"])
        df.to_csv(filename, index=False) # Write to CSV without row index