from datetime import datetime
import csv

# PS command to create a file: New-Item -ItemType file database.csv
tsf = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
bullet = input("What did you accomplish? ")
print(f"You entered: {bullet} at {tsf}")
row = [tsf,bullet]
file = open("database.csv", "w")
writer = csv.writer(file)
writer.writerow(row)
