"""
(Format an integer) Write a function with the following header to format the inte-
ger with the specified width.
def format(number, width):
The function returns a string for the number with prefix 0 s. The size of the string is
the width. For example, format(34, 4) returns "0034" and format(34, 5)
returns "00034". If the number is longer than the width, the function returns the
string representation for the number. For example, format(34, 1) returns "34".
Write a test program that prompts the user to enter a number and its width and dis-
plays a string returned from invoking format(number, width).

Sample Run:
Enter an integer: 34
Enter the width: 4
The formatted number is 0034
"""
def format(number: int, width: int) -> str:
    # return f"{number:0{width}d}" # methode 1
    num = str(number)
    if len(num) < width:
        return "0" * (width - len(num)) + num
    else:
        return num

def main():
    integer = eval(input("Enter an integer: "))
    width = eval(input("Enter the width: "))
    print(f"The formatted number is {format(integer, width)}")

main()