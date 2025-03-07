from datetime import datetime
import csv

# PS command to create a file: New-Item -ItemType file database.csv
tsf = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
bullet = input("What did you accomplish? ")
print(f"You entered: {bullet} at {tsf}")
row = [tsf,bullet]
with open("database.csv", "a", newline='\n') as file:
    writer = csv.writer(file)
    writer.writerow(row)
    file.close()

with open("database.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lines in csvFile:
        print(lines)