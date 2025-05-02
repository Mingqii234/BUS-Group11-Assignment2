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

def get_daily_building_consumption(building_id, date):
    records = load_energy_data('data/energy_data.csv')
    total = 0
    for r in records:
        if r.building_id == building_id and r.date == date:
            total += r.consumption_kwh
    return total

