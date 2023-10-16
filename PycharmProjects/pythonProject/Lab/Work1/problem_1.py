from os import system
print("\tWelcome To Distance Converter\t\n")

# Feet to Inches and Inches to Feet conversion
def feet_to_inches(feet):
    return feet * 12
def inches_to_feet(inches):
    return inches / 12

# Feet to Yards and Yards to Feet conversion
def feet_to_yards(feet):
    return feet / 3
def yards_to_feet(yards):
    return yards * 3

# Feet to Miles and Miles to Feet conversion
def miles_to_feet(miles):
    return miles * 5280
def feet_to_miles(feet):
    return feet / 5280

# Main Program
while True:
    choice = eval(input("Enter 1 for Feet to Inches and Inches to Feet conversion\n"
                        "Enter 2 for Feet to Yards and Yards to Feet conversion\n"
                        "Enter 3 for Feet to Miles and Miles to Feet conversion\n"
                        "Enter 4 to Exit\n"
                        "Enter your choice: "))
    if choice == 1:
        system("clear")
        sub_choice = eval(input("Enter 1 for Feet to Inches conversion\n"
                                "Enter 2 for Inches to Feet conversion\n"
                                "Enter your choice: "))
        if sub_choice == 1:
            feet = eval(input("Enter the value in feet: "))
            print("The value in inches is: ", feet_to_inches(feet))
        elif sub_choice == 2:
            inches = eval(input("Enter the value in inches: "))
            print("The value in feet is: ", inches_to_feet(inches))
        else:
            print("Invalid Choice\n")
    elif choice == 2:
        system("clear")
        sub_choice = eval(input("Enter 1 for Feet to Yards conversion\n"
                                "Enter 2 for Yards to Feet conversion\n"
                                "Enter your choice: "))
        if sub_choice == 1:
            feet = eval(input("Enter the value in feet: "))
            print("The value in yards is: ", feet_to_yards(feet))
        elif sub_choice == 2:
            yards = eval(input("Enter the value in yards: "))
            print("The value in feet is: ", yards_to_feet(yards))
        else:
            system("clear")
            print("Invalid Choice\n")
    elif choice == 3:
        system("clear")
        sub_choice = eval(input("Enter 1 for Feet to Miles conversion\n"
                                "Enter 2 for Miles to Feet conversion\n"
                                "Enter your choice: "))
        if sub_choice == 1:
            feet = eval(input("Enter the value in feet: "))
            print("The value in miles is: ", feet_to_miles(feet))
        elif sub_choice == 2:
            miles = eval(input("Enter the value in miles: "))
            print("The value in feet is: ", miles_to_feet(miles))
        else:
            system("clear")
            print("Invalid Choice\n")
    elif choice == 4:
        print("Exiting...\n")
        break
    else:
        system("clear")
        print("Invalid Choice\n")



