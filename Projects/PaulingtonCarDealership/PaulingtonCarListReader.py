import os
import csv
from tabulate import tabulate

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "Database.csv")

# Read the contents of the CSV file
with open(db_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Read the header row
    data = list(reader)     # Read the remaining data

# Display the table using tabulate
print(tabulate(sorted(data), headers=headers, tablefmt="grid"))