import random
from energy_alert import RoomStatus, EnergyAlertSystem
from energy_data import DataGeneratorFactory
from visualizer import EnergyVisualizer


def scan_and_alert(rooms, alerter):
    for room in rooms:
        alerter.update(room)

def main():
    factory = DataGeneratorFactory()
    viz = EnergyVisualizer()
    for period in ["daily", "weekly", "monthly"]:
        data = factory.create(period).generate()
        title = f"{period.capitalize()} Energy Usage"
        viz.plot_data_with_percent(data, title)

    print("\n=== Energy Alert Simulation (Single Scan) ===")
    room_names = ["Room A", "Room B", "Room C"]
    rooms = []
    alerter = EnergyAlertSystem()

    for name in room_names:
        occupied = random.choice([True, False])
        light = random.choice([True, False])
        ac = random.choice([True, False])
        r = RoomStatus(name, is_occupied=occupied, light_on=light, ac_on=ac)
        rooms.append(r)

    scan_and_alert(rooms, alerter)


if __name__ == "__main__":
    main()