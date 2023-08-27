# Importing Random Module
import random

# Welcome Script
print("Welcome To Rock-Paper-Scissors\n")

# Initialize win, lose, and tie counts
win = 0
lose = 0
tie = 0

# Choices for Rock, Paper, Scissors
choices = ["Rock", "Paper", "Scissors"]

while True:
    print("1 for Rock\n2 for Paper\n3 for Scissors")

    user_choice = input("Choose your move: ")

    if user_choice in ["1", "2", "3"]:
        user_choice = int(user_choice)
        computer_choice = random.randint(1, 3)

        print(f"You chose: {choices[user_choice - 1]}")
        print(f"Computer chose: {choices[computer_choice - 1]}")

        if user_choice == computer_choice:
            print("It's a tie!")
            tie += 1
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print("You win!")
            win += 1
        else:
            print("Computer wins!")
            lose += 1

        # Display updated win, lose, and tie counts
        print(f"Total Wins: {win}, Losses: {lose}, Ties: {tie}\n")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break
    else:
        print("Invalid input. Please choose 1, 2, or 3.")
