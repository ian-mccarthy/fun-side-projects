#Simple rock paper scissors game between user and the computer's randomly generated responses

import random
import time

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Choose rock paper or scissors! \nOr Q to quit the game\n").lower()
    if user_choice == "q":
        break

    if user_choice not in options:
        print("Invalid choice")
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_choice = options[random_number]
    print("Computer picked", computer_choice)

    if user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        user_wins += 1
        time.sleep(1.5)

    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        user_wins += 1
        time.sleep(1.5)

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        user_wins += 1
        time.sleep(1.5)
    
    elif user_choice == computer_choice:
        print("It's a draw")    
    
    else:
        print("You lose!")
        computer_wins += 1
        time.sleep(1.5)

print("You won", user_wins, "times")
print("The computer won", computer_wins, "times")

print("Thanks for playing!")

