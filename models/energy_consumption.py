
class EnergyConsumption:
    def __init__(self, building_id: int, date: str, consumption_kwh: float):
        self.building_id = building_id
        self.date = date
        self.consumption_kwh = consumption_kwh

    def __repr__(self):
        return f"EnergyConsumption(building_id={self.building_id}, date='{self.date}', consumption_kwh={self.consumption_kwh})"