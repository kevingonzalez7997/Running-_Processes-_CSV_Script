import psutil
import os
import csv

csv_file = "processes_info.csv"

with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["pid", "name", "exe", "cpu_percent", "memory"], extrasaction='ignore')
    writer.writeheader()

    for process in psutil.process_iter(attrs=['pid', 'name', 'exe', 'memory_info', 'cpu_percent']):
        pinfo = process.info
        writer.writerow(pinfo)
