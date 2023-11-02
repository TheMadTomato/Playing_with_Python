# convert decimal to hexadecimal
decimal_value = int(input("Enter a decimal number: "))
output = ''
while decimal_value > 0:
    remainder = decimal_value % 16

    if 0 <= remainder <= 9:
        output = str(remainder) + output
    elif remainder == 10:
        output = 'A' + output
    elif remainder == 11:
        output = 'B' + output
    elif remainder == 12:
        output = 'C' + output
    elif remainder == 13:
        output = 'D' + output
    elif remainder == 14:
        output = 'E' + output
    elif remainder == 15:
        output = 'F' + output
    decimal_value = decimal_value // 16

print(output)

#######################################################################
"""
# convert decimal to hexadecimal
decimal_value = int(input("Enter a decimal number: "))
output = ''
while decimal_value > 0:
    remainder = decimal_value % 16

    if 0 <= remainder <= 9:
        output = str(chr(remainder + ord('0'))) + output
    else:
        output = str(chr(remainder - 10 + ord('A')))

    decimal_value = decimal_value // 16

print(output)

"""




