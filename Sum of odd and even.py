x=int(input('Enter the value of x: '))
y=int(input('Enter the value of y: '))

num = list(range(x, y))

even = num[::2]
odd = num[1::2]

print('Even list:', even)
print('Odd list:', odd)

print('Even:', sum(even))
print('Odd:', sum(odd))



