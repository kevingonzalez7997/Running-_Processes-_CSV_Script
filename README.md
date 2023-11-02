# Process Information to CSV
### Kevin Gonzalez

This Python script allows you to gather information about running processes on your system and save it to a CSV file. It utilizes the `psutil` library to collect data on each process, including process ID (PID), name, executable path (exe), memory usage, and CPU usage.

## How to Use

1. Run the script.
2. It will create a CSV file named `processes_info.csv` to store the process information.
3. The script iterates over running processes, extracts the specified attributes, and writes them to the CSV file.

The resulting CSV file provides a snapshot of the currently running processes and their resource utilization.

## Requirements

- Python
- psutil library (You can install it using `pip install psutil`)
