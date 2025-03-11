from datetime import datetime
from pyfiglet import Figlet
import csv
import os

f = Figlet(font='larry3d')
print(f.renderText('Weekly'))
print(f.renderText('Bullets'))

# https://pypi.org/project/simple-term-menu/

def find_db():
    cwd = os.getcwd()
    fullPath = cwd + "\\database.csv"
    if os.path.isfile(fullPath):
        print("database.csv exists")
    else:
        print('database.csv DOES NOT exist. Need to create, one second')
        headers = ["ID","Timestamp","Bullet"]
        with open("database.csv", "w") as file:
            dw = csv.DictWriter(file, delimiter=',', fieldnames=headers)
            dw.writeheader()

def get_bullet():
    # PS command to create a file: New-Item -ItemType file database.csv
    tsf = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bullet = input("What did you accomplish? ")
    print(f"You entered: {bullet.strip()} at {tsf}")
    print("\r")
    row = ["555",tsf,bullet.strip()]
    with open("database.csv", "a", newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(row)
        file.close()

def prn_db():
    print("Here are the current contents of your database...")
    print("\r")
    with open("database.csv", 'r') as fileRead:
        csvFile = csv.reader(fileRead)
        for lines in csvFile:
            print(lines)
    print("\r")

running = True
find_db()
while running == True:
    print("Select and option by entering the number of what you want to do:")
    op_1 = "Add a weekly accomplishment."
    print(f"1. {op_1}")
    op_2 = "Print the entire database."
    print(f"2. {op_2}")
    op_3 = "Exit this script."
    print(f"3. {op_3}")
    print("\r")

    selection = input()
    if selection == "1":
        print(f"You selected {selection}. {op_1}")
        print("\r")
        get_bullet()
    elif selection == "2":
        print(f"You selected {selection}. {op_2}")
        print ("\r")
        prn_db()
    elif selection == "3":
        print(f"You selected {selection}. {op_3}")
        print("\r")
        running = False
    else:
        print("Looks like you entered a number that isn't one of the options. BYE BYE!")
        print("\r")


