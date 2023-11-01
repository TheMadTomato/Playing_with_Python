"""
Turn To Hexadecimal
"""

# Turn To Hexadecimal method 1
decimal = int(input("Enter a decimal number: "))
hex = list()
while decimal > 0:
    remainder = decimal % 16
    if remainder == 10:
        remainder = "A"
    elif remainder == 11:
        remainder = "B"
    elif remainder == 12:
        remainder = "C"
    elif remainder == 13:
        remainder = "D"
    elif remainder == 14:
        remainder = "E"
    elif remainder == 15:
        remainder = "F"
    hex.append(str(remainder))
    decimal = decimal // 16

output = "".join(hex[::-1])
print(output)

# Turn To Hexadecimal method 2
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:
        return chr(hexValue - 10 + ord('A'))
def decimal_to_hex(decimalvalue):
    hex = ""
    while decimalvalue != 0:
        hexValue = decimalvalue % 16
        hex = toHexChar(hexValue) + hex
        decimalvalue = decimalvalue // 16
    return hex

def main():
    decimalvalue = eval(input("Enter a decimal number: "))
    print("The hex number for decimal", decimalvalue, "is", decimal_to_hex(decimalvalue))

main()