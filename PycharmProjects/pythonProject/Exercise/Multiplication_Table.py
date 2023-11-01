# print title
print("\t\t Multiplication Table")

# display the number from 1 to 10
print("   ", end = '')
for j in range(1, 10):
    print("  ", j, end = '')
print() # jump to next line
print("-" * 39)

# display the table body
for i in range(1, 10):
    print(i, "|", end = '')
    for j in range(1, 10):
        # display the product and align properly
        print(format(i * j, "4d"), end = '')
    print() # jump to next line

