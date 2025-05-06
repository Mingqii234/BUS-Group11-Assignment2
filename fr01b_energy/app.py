from flask import Flask, render_template
from energy_system import EnergySystem
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

    # 准备模板数据（将datetime对象格式化为字符串方便显示）
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

    return render_template("dashboard.html", buildings=buildings_data)
    

if __name__ == '__main__':
    app.run(debug=True)