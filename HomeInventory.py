# ------------------------------------------------
# Title: Home Inventory script 2.0
# Date: April 30th 2023
# ------------------------------------------------
# Header so reader knows which version of home inventory they are using
print("Welcome to Home Inventory 2.0!")

# Define variable menu_choice for user input to navigate menu
menu_choice = 0

# Define list to capture user input for home inventory
home_inventory = []


# Define function to display the menu
def display_menu():
    print("Menu of options\n",
          "1) Add data to list\n",
          "2) Display current data\n",
          "3) Exit and save to file\n")


# Define function 1 to enter new item/value as a Tuple to home_inventory list
def add_items():
    print("\n" + "Enter the price and value of each item.  Type 'Exit' to quit.")
    while True:
        item_name = input("What is the name of the item? ").capitalize()
        if item_name == "Exit":
            break
        else:
            item_value = float(input("What is the value of the item? "))
            item_value = format(item_value, '.2f')
            # Create the Tuple list_item
            list_item = (item_name, item_value)
            # Append the Tuple to the list home_inventory
            home_inventory.append(list_item)


# Define function 2 to print the Tuples within the list home_inventory
def print_list():
    print("Name \tValue")
    for item in home_inventory:
        item_name, item_value = item
        print(item_name + "\t" + "$" + item_value)


# Define function 3 to save list to HomeInventory text file and exit
def save_exit():
    text_file = open("HomeInventory.txt", "w")
    text_file.write("Name \tValue \n")
    for item in home_inventory:
        item_name, item_value = item
        item_string = item_name + "\t" + "$" + item_value + "\n"
        text_file.write(item_string)
    text_file.close()
    exit()


# Run program
display_menu()
while True:
    menu_choice = int(input("Enter 1, 2, or 3 "))
    if menu_choice == 1:
        add_items()
    elif menu_choice == 2:
        print_list()
    elif menu_choice == 3:
        save_exit()
    else:
        print("Invalid choice")
        display_menu()
