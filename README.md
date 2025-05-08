# BUS-Group11-Assignment2
BUS-Group11-Assignment2

## 4. Summary of Implemented Functionalities
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


###  [Other Components](./main.py)

#### `main.py` – System Orchestration and Demonstration

The `main.py` file serves as the central controller that integrates and demonstrates the core functionalities of the system:

- Initializes example `RoomStatus` objects and runs the alert system via `scan_and_alert()`.  
- Generates energy usage data for daily, weekly, and monthly periods.  
- Visualizes simulated data using `plot_data()`.  
- Coordinates execution flow, providing a simple unified entry point for users.



  
