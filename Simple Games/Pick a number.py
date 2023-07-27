from random import*

def pikanum(name1, name2, round):
    #register the chosen numbers
    # name1 = input("Player 1: ")
    # name2 = input("Player 2: ")
    print("\nRules: Enter a number between 1 and 25.\n")
    


    i = round
    n1 = 0
    n2 = 0

    while i != 0:

        num1 = int(input(f'{name1} enter your number: '))
        num2 = int(input(f'{name2} enter your number: '))
        print()
        ran_num = randrange(1, 25)

        #main loop
        if num1 == ran_num:
            print(f'The Winning number is {ran_num}.\n{name1} chose {num1}, thus he wins!\nTotal={n1}\n')
            n1 += 2
            
        else:
            print(f'The Winning number is {ran_num}.\n{name1} chose {num1}, thus he loses!\nTotal={n1}\n')
            
            
        if num2 == ran_num:
            print(f'The Winning number is {ran_num}.\n{name2} chose {num2}, thus he wins!\nTotal={n2}\n')
            n2 += 2
            
        else:
            print(f'The Winning number is {ran_num}.\n{name2} chose {num2}, thus he loses!\nTotal={n2}\n')
            
        i -= 1
    
   
pikanum("Paul","Patrick",1)

