n=int(input("enter a number:"))

for fizzbuzz in range(1, n):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0: 
        print("buzz")
        continue
    print(fizzbuzz)