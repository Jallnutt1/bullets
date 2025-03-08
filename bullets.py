from datetime import datetime
from pyfiglet import Figlet
import csv
import os.path

f = Figlet(font='larry3d')
print(f.renderText('Weekly'))
print(f.renderText('Bullets'))

# https://pypi.org/project/simple-term-menu/


if os.path.isfile("C:\\Users\\Jason\\Documents\\bullets\\database.csv"):
    print("database.csv exists")
else:
    print('database.csv DOES NOT exist. Need to create, one second')
    file = open("database.csv", "x")
    file.close()

print("""
Select and option:
1. Add a weekly accomplishment
2. Print the database
3. Something else
""")

selection = input()
print(f"You selected {selection}")

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