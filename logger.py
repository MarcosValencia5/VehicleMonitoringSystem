import csv
from datetime import datetime
import os

LOG_FILE = "vehicle_log.csv"

def log_data(data):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "speed", "rpm", "coolant_temp"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            data["speed"],
            data["rpm"],
            data["coolant_temp"]
        ])