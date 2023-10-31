"""
You have a bowl on your counter with an even number of pieces of fruit in it. Half of them are bananas, and the other half are apples. You need 3 apples to make a pie.

Task
Your task is to evaluate the total number of pies that you can make with the apples that are in your bowl given to total amount of fruit in the bowl.

Input Format
An integer that represents the total amount of fruit in the bowl.

Output Format
An integer representing the total number of whole apple pies that you can make.

Sample Input
26

Sample Output
4
"""

#input number of fruits that should be even
while True:
    try:
        total_fruits = int(input("Enter number of fruits: "))
        if total_fruits % 2 == 0:
            break
    except ValueError:
        print("Total number of fruits should be even")

#Divide the total number of fruits by 2 to get the number of apples
apples = bananas = total_fruits // 2

#evaluate the numbers of apple pie that i can make
pies = apples // 3

#output the number of apple pies that i can make
print(f"I can make {pies} apple pies")