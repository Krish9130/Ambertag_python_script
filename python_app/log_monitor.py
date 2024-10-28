import re
import time
import csv
import os

# Define the path to the nohup.out file and the CSV file
nohup_file = 'app.out'
csv_file = 'log_extraction.csv'

# Regular expression to match the IP address and date from the log
log_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(\d{2}\/[A-Za-z]{3}\/\d{4} \d{2}:\d{2}:\d{2})\]')

def extract_ip_and_date(line):
    # Extract the IP address and date from the log line
    match = log_pattern.search(line)
    if match:
        ip_str = match.group(1)
        date_str = match.group(2)
        return ip_str, date_str
    return None, None

def write_to_csv(ip, date):
    # Avoid adding duplicate entries to the CSV file
    with open(csv_file, 'a+', newline='') as csvfile:
        csvfile.seek(0)
        reader = csv.reader(csvfile)
        for row in reader:
            if row and row[0] == ip and row[1] == date:
                return  # Skip duplicate entry

        # Append new entry
        writer = csv.writer(csvfile)
        writer.writerow([ip, date])

def monitor_log_file():
    last_position = 0

    while True:
        with open(nohup_file, 'r') as f:
            f.seek(last_position)  # Move to the last read position
            new_entries = f.readlines()
            if new_entries:
                # Only take the first line of new entries
                first_line = new_entries[0]
                ip, date = extract_ip_and_date(first_line)
                if ip and date:
                    write_to_csv(ip, date)
                    print(f"Stored IP: {ip}, Date: {date} to {csv_file}")
            
            # Update the last position
            last_position = f.tell()

        time.sleep(1)  # Wait before checking for new entries

if __name__ == "__main__":
    # Clear the CSV file before starting
    open(csv_file, 'w').close()
    monitor_log_file()

