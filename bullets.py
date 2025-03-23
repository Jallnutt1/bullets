from datetime import datetime
from pyfiglet import Figlet
import csv
import os

f = Figlet(font='larry3d')                                                  # This print the big titles when you first run the script. 
print(f.renderText('Weekly'))
print(f.renderText('Bullets'))

                                                                            # https://pypi.org/project/simple-term-menu/

def find_db():                                                              # This function verifies if a 'database.csv' file exists the PWD. 
                                                                            # If not, the script creates such a file. 
    cwd = os.getcwd()
    fullPath = cwd + "\\database.csv"
    if os.path.isfile(fullPath):
        print("database.csv exists")
    else:
        print('database.csv DOES NOT exist. Need to create, one second')
        headers = ["ID","Timestamp","Bullet"]                               # The CSV has three columns, an 'ID', a 'Timestamp', and the actualy user 
                                                                            # input.
        with open("database.csv", "w", newline='') as file:
            dw = csv.DictWriter(file, fieldnames=headers)                   # Not sure why I used a 'DictWriter' versus a regular writer. Something 
                                                                            # to look into later. 
            dw.writeheader()

def get_bullet():                                                           # This function asks the user to input an accomplishment from the week. 
                                                                            # PS command to create a file: New-Item -ItemType file database.csv
    with open("database.csv", newline='') as fileRead:                      # This 'with' statement reads the csv files to get the number of rows.
        reader = csv.reader(fileRead)
        idNum = len(list(reader))                                           # The number of rows, including the header row is stored to 'idNum'. 
    tsf = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bullet = input("What did you accomplish? ")
    print(f"You entered: {bullet.strip()} at {tsf}")
    print("\r")

    row = [idNum,tsf,bullet.strip()]                                        # This is confusing, the value, 'idNum', that is stored in the 'ID' 
                                                                            # field of the current input is the current number of rows 
                                                                            # including the header row before the new input is added. 
                                                                            # For example, when the first input is added, the current number 
                                                                            # of rows is 1, the header row. 1 is what gets saved to the first 
                                                                            # input row from the user. 

    with open("database.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)
        file.close()

def prn_db():                                                               # This function prints the entire database to the terminal winddow
    print("Here are the current contents of your database...")
    print("\r")
    with open("database.csv", 'r') as fileRead:
        csvFile = csv.reader(fileRead)
        for lines in csvFile:
            print(lines)
    print("\r")

running = True
find_db()
while running == True:                                                      # The script keeps looping through until the user chooses the 'exit' option
    print("Select an option by entering the number of what you want to do:")
    op_1 = "Add a weekly accomplishment."
    print(f"1. {op_1}")
    op_2 = "Print the entire database."
    print(f"2. {op_2}")
    op_3 = "Exit this script."
    print(f"3. {op_3}")
    print("\r")

    selection = input()
    if selection == "1":                                                    # The options are 1, 2, and 3, however, this script keeps the input from the
                                                                            # user as a 'str' and compares the input to 1, 2, and 3 as strings. 
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

os.system('cls' if os.name == 'nt' else 'clear')                            # This line clears the termianl screen after the user has selected the exit
                                                                            # option.


