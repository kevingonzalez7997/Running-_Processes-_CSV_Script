import psutil
import os
import csv

# Define the name of the CSV file to be created
csv_file = "processes_info.csv"

# Open the CSV file for writing
with open(csv_file, 'w', newline='') as file:
    # Initialize a DictWriter, taking a list of dictionary 
    writer = csv.DictWriter(file, fieldnames=["pid", "name", "exe", "memory", "CPU"], extrasaction='ignore')
    # Write the header row in the CSV file
    writer.writeheader()
    # Iterate over the running processes with specific attributes
    for process in psutil.process_iter(attrs=['pid', 'name', 'exe', 'memory_info', 'cpu_percent']):
        # Access the info dictionary. This is automatically returned by the psutil.process_iter command by default 
        pinfo = process.info
        # Write the information for the current process to the CSV file
        writer.writerow(pinfo)
