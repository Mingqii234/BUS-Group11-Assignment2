from flask import Flask, render_template
from models.energy_system import EnergySystem
import os

app = Flask(__name__)

@app.route('/')
def index():
    system = EnergySystem(
        building_ids=["Library", "DormA", "Engineering"],
        device_types=["AC", "Light", "Computer", "Heater"]
    )
    system.simulate_data(num_days=10)

    if not os.path.exists("static"):
        os.makedirs("static")
    system.export_to_csv("static/energy_report.csv")

    return render_template("dashboard.html", buildings=system.buildings)

if __name__ == '__main__':
    app.run(debug=True)