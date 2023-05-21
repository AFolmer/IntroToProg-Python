# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# AFolmer,5.20.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# Open To Do List file, append current data to lstTable, close To Do List
try:
    with open(objFile, "r") as currentlist:
        for task in currentlist:
            row = task.split(",")
            dicRow = {"Item": row[0], "Priority": row[1]}
            lstTable.append(dicRow)
        currentlist.close()
# Try/except used here to let user know if they don't have a to-do list file
except:
    print("You do not have an existing to-do list.")


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        # Notify user if to-do list is empty
        if len(lstTable) == 0:
            print("Your to-do list is empty")
        # Print formatted to-do list
        else:
            print("Item \t Priority")
            for task in lstTable:
                print(task["Item"] + "\t" + task["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        # Obtain user input: list item and priority
        task = input("What is the name of the item? ")
        # Check to see if item is already in to-do list
        if task in lstTable:
            print("This item is already in your list.")
        # Obtain priority and enter item into list
        else:
            priority = input("What is the item priority? ")
            dicRow = {"Item": task, "Priority": priority}
            lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        # Check to see if there is data in table to remove
        if len(lstTable) == 0:
            print("Your to-do list is empty")
        # Remove item from table
        else:
            task = input("Enter the item to remove: ")
            remove = 0  # Internal variable to check that item is in list and notify user
            for row in lstTable:
                if row["Item"] == task:
                    lstTable.remove(row)
                    remove = 1
            if remove == 0:
                print("Item not found.")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        # Create new save file or overwrite existing
        currentlist = open(objFile, "w")
        # Save dictionary rows as comma separated values
        for row in lstTable:
            strData = (row["Item"] + "," + row["Priority"] + "\n")
            currentlist.write(strData)
        currentlist.close()
        print("List saved")
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Good bye!")
        break  # and Exit the program
