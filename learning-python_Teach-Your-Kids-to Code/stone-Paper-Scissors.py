
import random
choices = ["stone", "paper", "scissors"]
print("Stone crushes scissors. Scissors cut paper. Paper covers stone.")
player = input("Do you want to be stone, paper, or scissors (or quit)?:  ")
while player != "quit":
    player = player.lower()
    computer = random.choice(choices)
    print("You chose " + player + ", and the computer chose " + computer + ".")
    if player == computer:
        print("It's a tie!")
    elif player == "stone":
        if computer == "scissors":
            print("You win!")
        else:
            print("Computer wins!")
    elif player == "paper":
        if computer == "stone":
            print("You win!")
        else:
            print("Computer wins!")
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("I think there was some error...")
    print()
    player = input("Do you want to be stone, paper, or scissors (or quit)?:  ")


