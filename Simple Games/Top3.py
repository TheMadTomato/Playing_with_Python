'''
III.Write a python program to compute the scholarship to distribute on the top 3 winners in an art exhibit. The program has to prompt the user to input the number of
   contributors and the donation granted by each contributor (Assume that all donations are equal). The total of the collected donations is distributed as prizes to the first 3 winners as follows:
-          First prize gets 50%.
-          Second prize gets 30%.
-          Third prize gets 20%.
The program has to display the total amount of the contributions to distribute and the prizes to grant to each of the 3 winners.
'''
nbc = int(input("Enter the nunmber of Contributers: "))
dc = int(input("How much did Each Contributer donate:$ "))
td = nbc * dc
print('The total of the contributions is: $ ', td)


while True: 
    r = input("Enters the competitor's ranks: ")#first, second, or third
    if r == "first":
        name=input("Enter your name: ")
        ftd = td*50/100
        print(name, ' ranked the ', r, " he/she won: $ ", ftd)
    elif r == "second":
        name1=input("Enter your name: ")
        std =td*30/100
        print(name1, ' ranked the ', r, " he/she won: $ ", std)
    elif r == "third":
        name2=input("Enter your name: ")
        ttd = td*20/100
        print(name2, ' ranked the ', r, " he/she won: $ ", ttd)
    else:
        name3= input("Enter your name: ")
        print(name3, " did not rank among the top 3, thus he/she will get nothing")
        break
    



    
