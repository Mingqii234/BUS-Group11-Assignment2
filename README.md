# BUS-Group11-Assignment2
BUS-Group11-Assignment2

## 1. System Overview

This system is developed to support energy monitoring and management in campus buildings such as dormitories, classrooms, and laboratories. It provides real-time tracking of energy use and visualizes daily, weekly, and monthly usage trends using numerical summaries and bar charts with percentage labels.

These visual insights help users understand how energy is being used over time and spot unusual patterns more easily.

In addition, the system includes a simple alert mechanism that detects when rooms are unoccupied but devices like lights or air conditioning are still on. The alert is displayed in the console, aiming to reduce unnecessary energy use and encourage more efficient behavior.

The system is built with a modular structure, separating data generation, visualization, and alert logic into different components. This makes the project easier to maintain, test, and expand in the future.

---

## 2. Step-by-Step Execution

### FR01 Real-Time Energy Monitoring
**Files:** `app.py`, `models/building.py`, `models/energy_system.py`, `templates/dashboard.html`, `static/style.css`

**Set up Environment**

**Step 1:** Initialize Energy System  
The `EnergySystem` class manages multiple buildings and devices. It simulates real-time energy data using randomized timestamps and energy values.
Ensure Python 3.8 or later is installed.

**Step 2:** Data Export  
Energy data is exported to a CSV file (`static/energy_report.csv`), which includes the building ID, device name, timestamp, and energy consumption.
(Recommended) Create a virtual environment:

**Step 3:** Web Dashboard  
The `app.py` provides a Flask-based web dashboard, allowing users to view total energy usage and query historical data by date.
```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
```

**Step 4:** Run the Application  
Execute `app.py` to launch the dashboard. Access the web interface by opening `http://localhost:<port>/` in your web browser. 

**Install Dependencies**

---

### FR02 Send Alert: Detecting Energy Waste in Empty Rooms  
**Files:** `energy_alert.py`, `main.py`

**Step 1:** Initialize Room Data  
In `main.py`, a list of `RoomStatus` objects is created, each representing a room with randomly assigned `occupied`, `light_on`, and `ac_on` states.

**Step 2:** Define Alert Logic  
The alert behavior is implemented in `energy_alert.py` using the **Observer Design Pattern**:
- `RoomStatus` is the **Subject**  
- `EnergyAlertSystem` is the **Observer**  
When the room status changes, the observer is notified and may issue alerts.

**Step 3:** Run Alert System  
Run `main.py` to trigger the alert system.

**Step 4:** Observe Warnings  
If a room is empty but has the light or AC on, an alert will be printed. Example output:
Alert: Room A is empty but light is ON!

---

### FR06 Energy Usage Trend Visualization  
**Files:** `main.py`, `energy_data.py`, `visualizer.py`

**Step 1:** Enable the Visualization Block  
In `main.py`, uncomment the visualization section to activate trend generation and plotting.

**Step 2:** Generate Simulated Data  
`DataGeneratorFactory` in `energy_data.py` simulates energy usage over daily, weekly, and monthly periods.

**Step 3:** Plot and View Results  
The function `plot_data_with_percent()` in `visualizer.py` displays bar charts with energy usage and percentage change compared to a baseline.

**Step 4:** Run `main.py`  
Execute `main.py` to view the simulated energy usage visualizations.

---

### Tests  
This project includes unit tests for 3 core features, covering both **positive and negative scenarios**:

- **Alert system:** Ensures alerts are triggered only when rooms are empty but lights or AC are on.
- **Trend visualization:** Verifies correct generation of simulated energy data over different time periods.
- **Energy System:** Validates correct data simulation, export functionality, and device energy tracking.
#### [Real-Time Energy Monitoring and Data Export](./models/energy_system.py)

**To run all tests**, use the following command in terminal:
pytest tests/

---
## 3. List of Programming Languages, Frameworks, and Tools Used  

- **Programming Languages:**  
  - Python 3.8+  

- **Frameworks and Libraries:**  
  - Flask (for web dashboard)  
  - Matplotlib (for data visualization)  
  - pytest (for testing)  

- **Tools and Utilities:**  
  - Virtualenv (for environment management)  
  - CSV (for data export and import)  

---

## 4. Summary of Implemented Functionalities

### [Real-Time Energy Monitoring and Data Export](./models/energy_system.py)

This module includes the main energy system logic, supporting the following key features:

- **Building and Device Simulation**  
  Each building contains multiple devices, each tracking energy consumption over time.
- **Energy Data Simulation**  
  Simulates energy usage data for multiple buildings and devices over a configurable time range.
- **Data Export to CSV**  
  Exports building-level energy data to a structured CSV file for further analysis.
- **Factory Pattern for Building Creation**  
  Utilizes a factory pattern for creating building instances (e.g., Dormitory, Laboratory, Classroom) based on building IDs.
- **Data Query via Web Interface**  
  Allows users to query historical energy consumption data through a web interface with date-based selection.

#### [Web Interface for Data Query](./app.py)

###  [Energy Alert System](./energy_alert.py)
The **Energy Alert** module monitors the real-time status of rooms to detect unnecessary energy consumption. It implements the following functionalities:
- **Room Status Tracking**  
  Each room is represented using the `RoomStatus` class, which stores whether the room is occupied and whether lights or air conditioning (AC) are turned on.
- **Alert Logic (Observer Pattern)**  
  The `EnergyAlertSystem` class observes changes in room status. If a room is unoccupied and either the light or AC is on, an alert message is printed.
- **Detailed Alerts**  
  Alerts clearly indicate which devices are on (light, AC, or both), allowing for better response and diagnosis of energy waste.
- **Batch Alert Scanning**  
  The system supports batch processing of multiple rooms via the `scan_and_alert()` function, ensuring that only rooms with anomalies are reported.

###  [Energy Data Generation, Trends & Visualization](./energy_data.py)
This module includes both the **energy data generation logic** (`energy_data.py`) and **data visualization** (`visualizer.py`). It provides the following functionalities:
####  Data Generation (in `energy_data.py`)
- **Period-Based Data Generation**  
  A `DataGeneratorFactory` dynamically creates one of three generator classes (`DailyDataGenerator`, `WeeklyDataGenerator`, `MonthlyDataGenerator`) based on the selected time period.
- **Simulated Data Output**  
  Each generator produces a list of integer values representing hourly (daily), daily (weekly), or daily (monthly) energy consumption. These values fall within a configurable range, simulating realistic fluctuations.
- **Modular and Extensible Design**  
  Each data generator is a separate class, following the principle of single responsibility and enabling easy extension to future time scales (e.g., yearly).
- **Clean Interface**  
  Users interact with simple and abstracted methods like `generate()`, without needing to understand internal logic.

####  Data Visualization (in [`visualizer.py`](./visualizer.py))
- **Trend Plotting with Matplotlib**  
  The `plot_data()` function visualizes energy usage over time, generating clear line charts for daily, weekly, or monthly periods.
- **Integrated with Data Module**  
  Visual output is directly based on data produced by the energy data generators, enabling a smooth data-to-visual insight pipeline.
- **Customizable Axes and Labels**  
  The visualization includes proper axis labels, titles, and scaling for each period, enhancing readability and interpretability.

### [Web Interface for Data Query](./app.py)

This module provides a simple, interactive web interface for real-time data monitoring:

- **Date-Based Query**  
  Users can select a date to view the energy consumption of each building on that day.
- **CSV Data Download**  
  Provides a direct link to download the latest exported energy data file.

#### [Other Components](./models/building.py)
- **Building and Device Classes**  
  Includes a flexible building hierarchy with specialized building types (Dormitory, Laboratory, Classroom).
- **Factory Design Pattern**  
  Uses a factory pattern for building instance creation, improving code organization and scalability.

#### [Testing](./tests/)
- **Positive and Negative Test Cases**  
  Covers key functionalities such as data export, energy simulation, and device energy tracking.
- **Automated Test Execution**  
  Allows for easy test execution using the `unittest` module.



###  [Other Components](./main.py)

#### `main.py` – System Orchestration and Demonstration

The `main.py` file serves as the central controller that integrates and demonstrates the core functionalities of the system:



- Initializes example `RoomStatus` objects and runs the alert system via `scan_and_alert()`.  
- Generates energy usage data for daily, weekly, and monthly periods.  
- Visualizes simulated data using `plot_data()`.  
- Coordinates execution flow, providing a simple unified entry point for users.


---

## 5. Contribution Percentage to the Project

| Student Name & ID | Contribution (%) | Key Contributions/Tasks Completed | Comments (if any) | Signature |
|:-----------------|:----------------|:---------------------------------|:-----------------|:---------|
| Yu Zeng - 2810823 |       20%        |Implemented `main.py` for alert & trend features;<br>Add positive and negative test cases for trends in`test_energy_trends.py`;<br>Created step-by-step guide for alert & trend in README;<br>Demonstrated alert system in video|                   |Yu Zeng             |
|      Weitong Sun - 2608251             |      20%            |Developed building subclasses and optimized inheritance in `models/building.py`;<br>Enhanced `models/energy_system.py` to support datetime records;<br>Updated `tests/test_energy.py` for timestamp compatibility;<br>Built date-based energy data query and real-time display in `app.py` and `templates/dashboard.html`;<br>Demonstrated FR01 in the demo video.                                   |                   |    Weitong Sun       |
|    Mingqi Pan - 2749735               |       20%           |Implemented `energy_data.py` and `visualizer.py` for data generation and trend visualization;<br>demonstrated the energy alert and visualization tests in the project video;<br>contributed the functionality summary section in the README.                                   |                   | Mingqi Pan |
|  Yanwen Wang - 2847662 | 20%              | - Created and refactored `app.py` for Flask web server and data export <br>- Developed `building.py` for core building hierarchy and factory pattern <br>- Optimized FR01 directory structure <br>- Developed `style.css` for web dashboard styling <br> - Wrote README sections for FR01 setup and execution <br>- Managed branch merges and conflict resolution |                                   | Yanwen Wang                    |
|| Mian Li - 2773117 | 20% | Implemented `energy_alert.py` for alert & trend features; <br>Added positive and negative test cases in `test_energy_alert.py`; <br>Created *System Overview* section in README; <br>Demonstrated energy trend visualization in project video. |  | Mian Li |                   |                  |                                   |                   |           |


  
