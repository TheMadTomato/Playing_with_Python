import openpyxl
import os

#Function to clear the terminal
def clear_ter():
    os.system('cls' if os.name == 'nt' else 'clear')

# Constants for item prices and token values
BEER_PRICE = 2
WINE_PRICE = 3
BLUE_WINE_PRICE = 4
BEER_TOKEN = "beer"
WHITE_WINE_TOKEN = "white"
RED_WINE_TOKEN = "red"
PINK_WINE_TOKEN = "pink"
BLUE_WINE_TOKEN = "blue"

# Conversion factor: 1 dollar = 100000 LBP
CONVERSION_FACTOR = 100000

# Function to convert from LBP to dollars
def lbp_to_dollars(amount_lbp):
    return amount_lbp / CONVERSION_FACTOR

# Function to convert from dollars to LBP
def dollars_to_lbp(amount_dollars):
    return amount_dollars * CONVERSION_FACTOR

# Initialize Counting Varibales
Beer_Counter = 0
White_Counter = 0
Red_Counter = 0
Pink_Counter = 0
Blue_Counter = 0

# Initialize variables for tracking sales and revenue
total_sales = 0
total_dollars = 0
total_lbp = 0

# Initialize dictionary for storing sales data
sales_data = {}

# Create a new Excel workbook and add a worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = "Sales Data"

# Set column headers
headers = ["Sale ID", "Item", "Quantity", "Money Paid", "Total Price"]
worksheet.append(headers)

# Function for calculating the total price of an order
def calculate_price(item, quantity):
    if item == BEER_TOKEN:
        return quantity * BEER_PRICE
    elif item in (WHITE_WINE_TOKEN, RED_WINE_TOKEN, PINK_WINE_TOKEN):
        return quantity * WINE_PRICE
    elif item == BLUE_WINE_TOKEN:
        return quantity * BLUE_WINE_PRICE
    else:
        raise ValueError("Invalid item")

# Function for processing a sale
def process_sale(item, quantity, money_paid, currency="dollars"):

    total_price = calculate_price(item, quantity)
    
    if currency == "lbp":
        money_paid = lbp_to_dollars(money_paid)
    
    if money_paid < total_price:
        raise ValueError("Insufficient funds")
    
    sale_id = len(sales_data) + 1
    sales_data[sale_id] = {
        "item": item,
        "quantity": quantity,
        "money_paid": money_paid,
        "total_price": total_price
    }

    global Beer_Counter, White_Counter, Red_Counter, Pink_Counter, Blue_Counter
    if item == BEER_TOKEN:
        Beer_Counter += quantity 
    elif item == WHITE_WINE_TOKEN:
        White_Counter += quantity
    elif item == RED_WINE_TOKEN:
        Red_Counter += quantity
    elif item == PINK_WINE_TOKEN:
        Pink_Counter += quantity
    elif item == BLUE_WINE_TOKEN:
        Blue_Counter += quantity
    
    global total_sales, total_dollars, total_lbp 
    total_sales += total_price
    total_dollars += total_price
    total_lbp += money_paid# * 100000

    # Add sale data to the Excel worksheet
    worksheet.append([sale_id, item, quantity, money_paid, total_price])

# Initialize the amount of money in the case
total_dollars = int(input("Input how much money there is in the case at start: "))

#Main Loop
#Main Loop
clear_ter()
condition = True
while condition:
    choice = str(input("Want to Proceed? "))

    if choice == "yes" or choice == "y" or choice == "Y":
        sale_items = []  # List to store items and quantities in this sale
        currency_choice = input("Choose currency (dollars or lbp): ").lower()

        while True:
            picked_item = str(input("Input picked item (or 'done' to finish): "))
            if picked_item == "done":
                break
            num_of_item = int(input("Input the quantity: "))
            sale_items.append((picked_item, num_of_item))

        if currency_choice == "lbp":
            money_to_pay_lbp = int(input("Input the amount of money paid in LBP: "))
            for item, quantity in sale_items:
                process_sale(item, quantity, money_to_pay_lbp, currency="lbp")
            total_lbp += money_to_pay_lbp  # Add money_paid to total_lbp only once
        else:
            money_to_pay = int(input("Input the amount of money paid in dollars: "))
            for item, quantity in sale_items:
                process_sale(item, quantity, money_to_pay)
        clear_ter()
        print("Sales Data:")
        for sale_id, sale_data in sales_data.items():
            print(f"Sale #{sale_id}:")
            print(f"  Item: {sale_data['item']}")
            print(f"  Quantity: {sale_data['quantity']}")
            print(f"  Money paid: ${sale_data['money_paid']}")
            print(f"  Return: ${sale_data['money_paid'] - sale_data['total_price']}")
            print(f"  Total price: ${sale_data['total_price']}")

    if choice == "no" or choice == "n" or choice == "N":
        condition = False

# Save the workbook to a file
workbook.save("sales_data.xlsx")

# Open the saved workbook for further editing
workbook = openpyxl.load_workbook("sales_data.xlsx")
worksheet = workbook.active

# Add a blank row for separation
worksheet.append([])

# Add a row for item summaries
item_summary_headers = ["Item", "Total Quantity Sold"]
worksheet.append(item_summary_headers)

item_summaries = [
    ("White Wine", White_Counter),
    ("Red Wine", Red_Counter),
    ("Pink Wine", Pink_Counter),
    ("Blue Wine", Blue_Counter)
]

for item, quantity_sold in item_summaries:
    worksheet.append([item, quantity_sold])

# Add a row for total dollars
worksheet.append(["Total Dollars", total_dollars])

# Add a row for total LBP
worksheet.append(["Total LBP", total_lbp])

# Save the workbook with updated summaries
workbook.save("sales_data.xlsx")


# Print sales data
clear_ter()
print("Sales Data:")
for sale_id, sale_data in sales_data.items():
    print(f"Sale #{sale_id}:")
    print(f"  Item: {sale_data['item']}")
    print(f"  Quantity: {sale_data['quantity']}")
    print(f"  Money paid: ${sale_data['money_paid']}")
    print(f"  Return: ${sale_data['money_paid'] - sale_data['total_price']}")
    print(f"  Total price: ${sale_data['total_price']}")

# Print total sold amount of each item
print("Beer: ", Beer_Counter)
print("White Wine: ", White_Counter)
print("Red Wine: ", Red_Counter)
print("Pink Wine: ", Pink_Counter)
print("Blue Wine: ", Blue_Counter)

# Print revenue data
print(f"Total sales: ${total_sales}")
print(f"Total dollars: ${total_dollars}")
print(f"Total LBP: {total_lbp:,}L.L")

