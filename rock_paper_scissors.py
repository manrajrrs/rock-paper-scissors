import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

player_choice = input("Please enter rock, paper or scissors:").lower()

while player_choice not in choices:
    player_choice = input(f"{player_choice} is not a valid input. Please enter rock, paper or scissors:").lower()

print(f"Computer chose {computer_choice}!")
    
if player_choice == computer_choice:
    print("It's a draw!")
    
elif    (player_choice == "rock" and computer_choice == "scissors") or \
        (player_choice == "paper" and computer_choice == "rock") or \
        (player_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
    
else:
    print("You lose...")