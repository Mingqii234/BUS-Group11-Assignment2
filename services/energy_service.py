import csv
from models.energy_consumption import EnergyConsumption

def load_energy_data(file_path):
    energy_data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            energy = EnergyConsumption(
                int(row['building_id']),
                row['date'],
                float(row['consumption_kwh'])
            )
            energy_data.append(energy)
    return energy_data

def get_daily_building_consumption(building_id, date, records=None):
    if records is None:
        records = load_energy_data('data/energy_data.csv')
    matching_records = []
    for r in records:
        if r.building_id == building_id and r.date == date:
            matching_records.append(r)

    if not matching_records:
        raise ValueError(f"No consumption data found for building {building_id} on {date}")

    total = 0.0
    for r in matching_records:
        total += r.consumption_kwh

    return total

