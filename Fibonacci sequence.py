num = int(input("Enter how many terms you wish to see: "))

def fib(n):
    n1, n2 = 0, 1
    i = 0

    if num <= 0: 
        print( "Please enter a positive integer")
    elif num == 1:
        print("Fibonacci sequence upto", num,":")
        print(n1)
    else:
        print("Fibonacci sequence: ")
        while i < num:
            print(n1)
            f = n1 + n2

            n1 = n2
            n2 = f
            i += 1

fib(num)
