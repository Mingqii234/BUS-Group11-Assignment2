from energy_system import EnergySystem
import energy_plotter as plotter
import os

if not os.path.exists("output"):
    os.makedirs("output")

system = EnergySystem(
    building_ids=["Library", "DormA", "Engineering"],
    device_types=["AC", "Light", "Computer", "Heater"]
)
system.simulate_data(num_days=10)
system.export_to_csv("static/energy_report.csv")

plotter.plot_total_energy(system.buildings)
plotter.plot_device_trends(system.buildings)
plotter.plot_building_pie_charts(system.buildings)