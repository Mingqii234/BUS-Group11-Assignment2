from flask import Flask, render_template, request
from energy_system import EnergySystem
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    system = EnergySystem(
        building_ids=["Library", "DormA", "Engineering"],
        device_types=["AC", "Light", "Computer", "Heater"]
    )
    system.simulate_data(num_days=10)

    if not os.path.exists("static"):
        os.makedirs("static")
    system.export_to_csv("static/energy_report.csv")

    buildings_data = []
    for building in system.buildings:
        latest_timestamp = None
        for device in building.devices:
            usage = device.get_usage_by_day()
            for timestamp, _ in usage:
                if latest_timestamp is None or timestamp > latest_timestamp:
                    latest_timestamp = timestamp
        buildings_data.append({
            "id": building.id,
            "first_timestamp": latest_timestamp.strftime("%Y-%m-%d %H:%M:%S") if latest_timestamp else "N/A",
            "total_energy": building.get_total_energy()
        })

    selected_date = None
    energy_on_date = None

    if request.method == 'POST':
        selected_date_str = request.form.get('selected_date')
        if selected_date_str:
            selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d").date()
            energy_on_date = []
            for building in system.buildings:
                building_data = {
                    "id": building.id,
                    "energy": 0
                }
                for device in building.devices:
                    for timestamp, energy in device.get_usage_by_day():
                        if timestamp.date() == selected_date:
                            building_data["energy"] += energy
                energy_on_date.append(building_data)

    return render_template("dashboard.html", buildings=buildings_data, selected_date=selected_date, energy_on_date=energy_on_date)
    

if __name__ == '__main__':
    app.run(debug=True)