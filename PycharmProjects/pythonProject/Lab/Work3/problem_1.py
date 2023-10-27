"""
Let’s play this GAME.
Write a python program to announce the winner between two players.
•
 First, we should enter total number of Marble. (Example: 20 marbles mean each player has
10 marbles in his pocket.
oooPlayer 1 start first
Announce the winner at the end of the program
Use for loop or while, and condition
"""


# Pre-requisite
def Odd_or_Even(number):
    return number % 2 == 0


# 1. Enter the total number of marbles
total_marbles = int(input("Enter the total number of marbles: "))

# 2. Divide the total number of marbles by 2
player1_marbles = total_marbles // 2
player2_marbles = total_marbles // 2

# Main Loop
while True:
    # 3. Player 1 starts first
    print(f"Player 1 has {player1_marbles} marbles\nPlayer 2 has {player2_marbles} marbles")
    while True:
        # A do while style of loop to make sure the player enters a valid number
        player1_picked_marbles = int(input("Player One : Enter Number of marble that you want to play with:  "))
        if player1_picked_marbles > player1_marbles:
            print("Invalid number of marbles. Try again.")
            continue
        else:
            break

    # 4. Player 2 guess if it is even or odd
    player2_guess = input("Player Two : Guess if the number is 0.even or 1.odd:  ")
    if Odd_or_Even(player1_picked_marbles) == Odd_or_Even(int(player2_guess)):
        print("Player Two wins!")
        player2_marbles += player1_picked_marbles
        player1_marbles -= player1_picked_marbles
    else:
        print("Player Two loses!")
        player1_marbles += player1_picked_marbles
        player2_marbles -= player1_picked_marbles

    # 5. Check if game is finished
    if player1_marbles != 0 and player2_marbles != 0:
        print("The game is not yet finished!")
        # 6. Player 2 starts first
        print(f"Player 1 has {player1_marbles} marbles\nPlayer 2 has {player2_marbles} marbles")
        while True:
            # A do while style of loop to make sure the player enters a valid number
            player2_picked_marbles = int(input("Player Two : Enter Number of marble that you want to play with:  "))
            if player2_picked_marbles > player2_marbles:
                print("Invalid number of marbles. Try again.")
            else:
                break

        # 7. Player 1 guess if it is even or odd
        player1_guess = input("Player One : Guess if the number is 0.even or 1.odd:  ")
        if Odd_or_Even(int(player1_guess)) == Odd_or_Even(player2_picked_marbles):
            print("Player One wins!")
            player1_marbles += player2_picked_marbles
            player2_marbles -= player2_picked_marbles
        else:
            print("Player One loses!")
            player2_marbles += player2_picked_marbles
            player1_marbles -= player2_picked_marbles

        # 8. Check if game is finished
        if player1_marbles != 0 and player2_marbles != 0:
            print("The game is not yet finished!")
        else:
            break
        continue
    else:
        break

