# Testing eval with integers
x = 5
print(eval('x+1'))
print(eval('x'))


# Testing type() with int and string
x= input("Enter your name?")
print(type(x))
x= eval(input("enter your age?"))
print(type(x))