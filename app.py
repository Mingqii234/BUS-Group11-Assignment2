from flask import Flask, render_template
from models.energy_system import EnergySystem
import os

app = Flask(__name__)

@app.route("/")
def index():
    if not os.path.exists("output"):
        os.makedirs("output")

    system = EnergySystem(
        building_ids=["Dormitory", "Laboratory", "Classroom"],
        device_types=["AC", "Light", "Computer", "Heater"]
    )
    system.simulate_data(num_days=10)
    system.export_to_csv("static/energy_report.csv")

    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)