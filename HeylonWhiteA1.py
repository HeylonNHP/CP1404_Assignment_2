"""
CP1404 Assignment 1 - 2016
Items for hire
Heylon White
https://github.com/HeylonNHP/Assignment_1
21/03/16
"""

ITEMS_FILE_NAME = "items.csv"
MENU = "Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit"

"""
Pseudocode function load_items:

function load_items(filename)
    file_lines_list = []
    open filename as file_in for reading

    for each line in filename.readlines()
        strip line
        line_item_list = split line by ","

        line_item_list[0] = string of line_item_list[0]
        line_item_list[1] = string of line_item_list[1]
        line_item_list[2] = float of line_item_list[2]
        line_item_list[3] = string of line_item_list[3]

        append line_item_list to file_lines_list

    close file_in
    return file_lines_list
"""
def load_items(filename):
    file_lines_list = []
    file_in = open(filename, "r")

    for line in file_in.readlines():
        line = line.strip()
        line_item_list = line.split(",")

        # ensure value types are correct
        line_item_list[0] = str(line_item_list[0])
        line_item_list[1] = str(line_item_list[1])
        line_item_list[2] = float(line_item_list[2])
        line_item_list[3] = str(line_item_list[3])

        file_lines_list.append(tuple(line_item_list))

    file_in.close()
    return file_lines_list

def save_items(items_list, filename):
    file_out = open(filename, "w")
    for item in items_list:
        file_out.write("{},{},{},{}".format(item[0], item[1], item[2], item[3]) + "\n")
    file_out.close()



"""
Pseudocode function hiring_an_item:

function hiring_an_item(items_list)
    count = 0
    items_available = False
        for each item in items_list
            if item[3] == "in"
                items_available = True
                item_description = item[0],item[1]
                display count,item_description,item[2]
            count += 1

            if items_available == False
                display No items available message
                return items_list

        display Enter item number

        try
            get item_choice
        except
            display Invalid input message
            return items_list

        if (item_choice >= 0 and item_choice < len(items_list)) and items_list[item_choice][3] == "in"
            items_list[item_choice] = (items_list[item_choice][0],items_list[item_choice][1],items_list[item_choice][2], "out")
            display items_list[item_choice][0],items_list[item_choice][2]
        else
            display Item not on hire message

        return items_list
"""
def hiring_an_item(items_list):
    count = 0
    items_available = False
    for item in items_list:
        if item[3] == "in":
            items_available = True
            item_description = "{} ({})".format(item[0], item[1])
            print("{} - {:39} = ${:7.2f}".format(count, item_description, item[2]))
        count += 1

    if items_available == False:
        print("No items are currently available for hire")
        return items_list

    print("Enter the number of an item to hire")

    try:
        item_choice = int(input(">>> "))
    except:
        print("Invalid input; enter a number")
        return items_list

    # check if item choice is inside the bounds of the list, and is currently not hired out
    if (item_choice >= 0 and item_choice < len(items_list)) and items_list[item_choice][3] == "in":
        items_list[item_choice] = (items_list[item_choice][0], items_list[item_choice][1], items_list[item_choice][2], "out")
        print("{} hired for ${:.2f}".format(items_list[item_choice][0], items_list[item_choice][2]))
    else:
        print("That item is not available for hire")

    return items_list

def returning_an_item(items_list):
    count = 0
    items_to_return = False
    for item in items_list:
        if item[3] == "out":
            items_to_return = True
            item_description = "{} ({})".format(item[0], item[1])
            print("{} - {:39} = ${:7.2f}".format(count, item_description, item[2]))
        count += 1

    if items_to_return == False:
        print("No items are currently on hire")
        return items_list

    print("Enter the number of an item to return")

    valid_input = ""
    item_choice = -1
    try:
        item_choice = int(input(">>> "))
    except:
        print("Invalid input; enter a number")
        valid_input = False

    if valid_input == "":
        if (item_choice >= 0 and item_choice < len(items_list)):
            if items_list[item_choice][3] == "out":
                valid_input = True
            else:
                print("That item is not on hire")
                return items_list
        else:
            print("Invalid item number")


    while valid_input != True:
        valid_input = ""
        try:
            item_choice = int(input(">>> "))
        except:
            print("Invalid input; enter a number")
            valid_input = False

        if valid_input == "":
            if (item_choice >= 0 and item_choice < len(items_list)):
                if items_list[item_choice][3] == "out":
                    valid_input = True
                else:
                    print("That item is not on hire")
                    return items_list
            else:
                print("Invalid item number")

    items_list[item_choice] = (items_list[item_choice][0], items_list[item_choice][1], items_list[item_choice][2], "in")
    print("{} returned".format(items_list[item_choice][0]))
    return items_list

def add_new_item(items_list):
    item_name = input("Item name: ")
    while item_name == "":
        print("Input can not be blank")
        item_name = input("Item name: ")
    item_description = input("Description: ")
    while item_description == "":
        print("Input can not be blank")
        item_description = input("Description: ")

    item_price = ""
    try:
        item_price = float(input("Price per day: $"))
    except:
        print("Invalid input; enter a valid number")

    while item_price == "" or item_price <= 0:
        if item_price != "":
            print("Price must be >= $0")
            print("Invalid input; enter a valid number")
        try:
            item_price = float(input("Price per day: $"))
        except:
            print("Invalid input; enter a valid number")

    items_list.append((item_name, item_description, item_price, "in"))
    print("{} ({}), ${:.2f} now available for hire".format(item_name, item_description, item_price))
    return items_list


"""
Pseudocode function main:

function main()
    display Welcome message

    items_list = load_items(ITEMS_FILE_NAME)
    display length of items_list,ITEMS_FILE_NAME

    display menu
    get user_input (to lowercase)

    while user_input != "q"
        if user_input == "l"
            display Items on file
            count = 0

            for each item in items_list
                if item[0] == out
                    hire_status = "*"
                else
                    hire_status = ""

                item_description = item[0] + "(" + item[1] + ")"
                display count,item_description,item[2],hire_status
                count += 1

        else if user_input == "h"
            items_list = hiring_an_item(items_list)
        else if user_input == "r"
            (return an item)
        else if user_input == "a"
            items_list = add_new_item(items_list)
        else
            display Invalid menu choice message

        display menu
        get user_input (to lowercase)

    save_items(items_list,ITEMS_FILE_NAME)
    display Amount of items saved message
    display Goodbye message

"""
def main():
    print("Items for hire - By Heylon White")
    items_list = load_items(ITEMS_FILE_NAME)
    print("{} items loaded from {}".format(len(items_list),ITEMS_FILE_NAME))

    print(MENU)
    user_input = input(">>> ").lower()

    while user_input != "q":
        if user_input == "l":
            print("All items on file (* indicates item is currently out):")
            count = 0

            for item in items_list:
                if item[3] == "out":
                    hire_status = "*"
                else:
                    hire_status = ""

                item_description = "{} ({})".format(item[0], item[1])
                print("{} - {:39} = ${:7.2f} {}".format(count, item_description, item[2], hire_status))
                count += 1

        elif user_input == "h":
            items_list = hiring_an_item(items_list)
        elif user_input == "r":
            items_list = returning_an_item(items_list)
        elif user_input == "a":
            items_list = add_new_item(items_list)
        else:
            print("Invalid menu choice")
        print(MENU)
        user_input = input(">>> ").lower()

    save_items(items_list,ITEMS_FILE_NAME)
    print("{} items saved to {}".format(len(items_list), ITEMS_FILE_NAME))
    print("Have a nice day :)")

