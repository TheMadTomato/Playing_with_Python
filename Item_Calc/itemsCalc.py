import openpyxl

# Constants for item prices and token values
BEER_PRICE = 2
WINE_PRICE = 3
BLUE_WINE_PRICE = 4
BEER_TOKEN = "beer"
WHITE_WINE_TOKEN = "white"
RED_WINE_TOKEN = "red"
PINK_WINE_TOKEN = "pink"
BLUE_WINE_TOKEN = "blue"

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
headers = ["Sale ID", "Item", "Money Paid", "Total Price"]
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
def process_sale(item, quantity, money_paid):
    total_price = calculate_price(item, quantity)
    if money_paid < total_price:
        raise ValueError("Insufficient funds")
    
    sale_id = len(sales_data) + 1
    sales_data[sale_id] = {
        "item": item,
        "quantity": quantity,
        "money_paid": money_paid,
        "total_price": total_price
    }
    
    global total_sales, total_dollars, total_lbp
    total_sales += total_price
    total_dollars += money_paid
    total_lbp += money_paid * 100000

    # Add sale data to the Excel worksheet
    worksheet.append([sale_id, item, money_paid, total_price])

# Example usage
process_sale(BEER_TOKEN, 1, 3)  # Buy 1 beer for $3
process_sale(BLUE_WINE_TOKEN, 1, 4)  # Buy 1 blue wine for $4
process_sale(RED_WINE_TOKEN, 2, 6)  # Buy 2 red wines for $6

# Save the workbook to a file
workbook.save("sales_data.xlsx")

# Print sales data
print("Sales Data:")
for sale_id, sale_data in sales_data.items():
    print(f"Sale #{sale_id}:")
    print(f"  Item: {sale_data['item']}")
    print(f"  Quantity: {sale_data['quantity']}")
    print(f"  Money paid: ${sale_data['money_paid']}")
    print(f"  Total price: ${sale_data['total_price']}")

# Print revenue data
print(f"Total sales: ${total_sales}")
print(f"Total dollars: ${total_dollars}")
print(f"Total LBP: {total_lbp}")

