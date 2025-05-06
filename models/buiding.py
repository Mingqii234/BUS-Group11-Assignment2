from datetime import datetime
from typing import List, Tuple

class Device:
    # Initialize a new Device object with a name and building ID
    def __init__(self, name: str, building_id: str):
        self.name = name
        self.building_id = building_id
        self.usage_log: List[Tuple[datetime, float]] = []

    # Add a record of energy usage for a specific timestamp
    def add_usage(self, timestamp: datetime, energy: float):
        if not isinstance(energy, (int, float)) or energy < 0:
            raise ValueError("Energy must be a non-negative number.")
        self.usage_log.append((timestamp, energy))

    # Calculate and return the total energy consumed by this device
    def get_total_energy(self) -> float:
        return sum(e for _, e in self.usage_log)

    # Count the number of most recent days where usage exceeded a given threshold
    def get_recent_high_usage_days(self, threshold: float = 4.5, days: int = 3) -> int:
        recent_log = sorted(self.usage_log)[-days:] if len(self.usage_log) >= days else self.usage_log
        return sum(1 for _, energy in recent_log if energy > threshold)

    # Return a sorted list of all usage records by timestamp
    def get_usage_by_day(self) -> List[Tuple[datetime, float]]:
        return sorted(self.usage_log)

    # Return a string representation of the Device for debugging purposes
    def __repr__(self):
        return f"<Device name={self.name} building={self.building_id} usage_entries={len(self.usage_log)}>"


class Building:
    def __init__(self, building_id):
        self.id = building_id
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def get_total_energy(self):
        return sum(d.get_total_energy() for d in self.devices)

    def get_devices(self):
        return self.devices

    def device_energy_breakdown(self):
        return {d.name: d.get_total_energy() for d in self.devices}




#
class Dormitory(Building):
    pass

class Laboratory(Building):
    pass

class Classroom(Building):
    pass

class BuildingFactory:
    @staticmethod
    def create_building(building_type):
        if building_type == "Dormitory":
            return Dormitory("Dormitory")
        elif building_type == "Laboratory":
            return Laboratory("Laboratory")
        elif building_type == "Classroom":
            return Classroom("Classroom")
        else:
            raise ValueError(f"Unknown building type: {building_type}")