from models.energy_system import EnergySystem
import os

if not os.path.exists("output"):
    os.makedirs("output")

system = EnergySystem(
    building_ids=["Library", "DormA", "Engineering"],
    device_types=["AC", "Light", "Computer", "Heater"]
)
system.simulate_data(num_days=10)
system.export_to_csv("static/energy_report.csv")
