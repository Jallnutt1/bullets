from datetime import datetime
import csv
import os.path

if os.path.isfile("C:\\Users\\Jason\\Documents\\bullets\\database.csv"):
    print("database.csv exists")
else:
    print('database.csv DOES NOT exist. Need to create, one second')
    file = open("database.csv", "x")
    file.close()

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