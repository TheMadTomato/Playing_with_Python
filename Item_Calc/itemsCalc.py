import openpyxl

# Constants for item prices and token values
BEER_PRICE = 2
WINE_PRICE = 3
BLUE_WINE_PRICE = 4
BEER_TOKEN = 1
WHITE_WINE_TOKEN = 3
RED_WINE_TOKEN = 3
PINK_WINE_TOKEN = 3
BLUE_WINE_TOKEN = 1

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
headers = ["Sale ID", "Beer Tokens", "White Wine Tokens", "Red Wine Tokens", "Pink Wine Tokens", "Blue Wine Tokens", "Money Paid", "Total Price"]
worksheet.append(headers)

# Function for calculating the total price of an order
def calculate_price(beer_tokens, white_wine_tokens, red_wine_tokens, pink_wine_tokens, blue_wine_tokens):
    total_tokens = beer_tokens + white_wine_tokens + red_wine_tokens + pink_wine_tokens + blue_wine_tokens
    total_price = (beer_tokens * BEER_PRICE) + (white_wine_tokens * WINE_PRICE) + (red_wine_tokens * WINE_PRICE) + (pink_wine_tokens * WINE_PRICE) + (blue_wine_tokens * BLUE_WINE_PRICE)
    if total_tokens != (BEER_TOKEN + WHITE_WINE_TOKEN + RED_WINE_TOKEN + PINK_WINE_TOKEN + BLUE_WINE_TOKEN):
        raise ValueError("Invalid token combination")
    return total_price

# Function for converting dollars to LBP
def dollars_to_lbp(dollars):
    return dollars * 100000

# Function for processing a sale
def process_sale(money_paid, beer_tokens, white_wine_tokens, red_wine_tokens, pink_wine_tokens, blue_wine_tokens):
    total_price = calculate_price(beer_tokens, white_wine_tokens, red_wine_tokens, pink_wine_tokens, blue_wine_tokens)
    if money_paid < total_price:
        raise ValueError("Insufficient funds")
    sale_id = len(sales_data) + 1
    sales_data[sale_id] = {
        "beer_tokens": beer_tokens,
        "white_wine_tokens": white_wine_tokens,
        "red_wine_tokens": red_wine_tokens,
        "pink_wine_tokens": pink_wine_tokens,
        "blue_wine_tokens": blue_wine_tokens,
        "money_paid": money_paid,
        "total_price": total_price
    }
    global total_sales
    global total_dollars
    global total_lbp
    total_sales += total_price
    total_dollars += money_paid
    total_lbp += dollars_to_lbp(money_paid)

    # Add sale data to the Excel worksheet
    worksheet.append([sale_id, beer_tokens, white_wine_tokens, red_wine_tokens, pink_wine_tokens, blue_wine_tokens, money_paid, total_price])

# Example usage
process_sale(6, 1, 0, 0, 0, 1) # Buy 1 beer and 1 blue wine for $6
process_sale(15, 0, 3, 0, 0, 0) # Buy 1 white wine, 1 red wine, and 1 pink wine for $15

# Save the workbook to a file
workbook.save("sales_data.xlsx")

# Print sales data
print("Sales Data:")
for sale_id, sale_data in sales_data.items():
    print(f"Sale #{sale_id}:")
    print(f"  Beer tokens: {sale_data['beer_tokens']}")
    print(f"  White wine tokens: {sale_data['white_wine_tokens']}")
    print(f"  Red wine tokens: {sale_data['red_wine_tokens']}")
    print(f"  Pink wine tokens: {sale_data['pink_wine_tokens']}")
    print(f"  Blue wine tokens: {sale_data['blue_wine_tokens']}")
    print(f"  Money paid: ${sale_data['money_paid']}")
    print(f"  Total price: ${sale_data['total_price']}")

# Print revenue data
print(f"Total sales: ${total_sales}")
print(f"Total dollars: ${total_dollars}")
print(f"Total LBP: {total_lbp}")

