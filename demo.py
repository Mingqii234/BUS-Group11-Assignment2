from services.energy_service import get_daily_building_consumption

usage = get_daily_building_consumption(building_id=1, date='2023-10-01')
print(f"Total daily energy consumption of building 1: {usage} kWh")