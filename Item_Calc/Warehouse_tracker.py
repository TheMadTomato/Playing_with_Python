import openpyxl
import os

#Function to clear the terminal
def clear_ter():
    os.system('cls' if os.name == 'nt' else 'clear')

# Create a new Excel workbook and add a worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = "Storage Data"

# Set Column headers
headers = ["Package", "Amount", "Min.Amount", "Added Amount"]
worksheet.append(headers)
# Initializing the pkgs variables

## Drinks pkgs
Beer_pkg = 2
White_Wine_pkgs = 0
Pink_Wine_pkgs = 0
Red_Wine_pkgs = 0
Blue_wine_pkgs = 0

## Non_drinks pkgs
Wine_Cups_pkgs = 0
Beer_Cups_pkgs = 0
Napkins_pkgs = 0

# Function to convert pkgs to unit per pkgs

def pkgToUnit(item):
    if item == "Beer_pkgs":
        return Beer_pkg*24
    elif item == "White_Wine_pkgs":
        return White_Wine_pkgs*6
    elif item == "Pink_Wine_pkgs":
        return Pink_Wine_pkgs*6
    elif item == "Red_Wine_pkgs":
        return Red_Wine_pkgs*6
    elif item == "Blue_Wine_pkgs":
        return Blue_Wine_pkgs*12
    elif item == "Wine_Cups_pkgs":
        return Wine_Cups_pkgs*24
    elif item == Beer_Cups_pkgs:
        return Beer_Cups_pkg*20
    elif item == "Napkins_pkgs":
        return Napkins_pkgs*50
    else:
        print("Invalid Input!")

# Data entry function to input what we have in the warehouse
###########################################################
# Test_1
print(pkgToUnit("Beer_pkgs"))
