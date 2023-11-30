import random

# Define the choices for the game
choices = 'stone', 'paper', 'scissor'

# Get the player's name
name = input("Enter your name: ")
print("All The Best " + name)

# Get the number of rounds to play
rounds = int(input("\nEnter the number of times you would like to play:"))

# Initialize scores for the player, computer, ties, and invalid inputs
user_score = 0
computer_score = 0
tied_score = 0
invalid_score = 0

# Loop for the specified number of rounds
for i in range(rounds):
    # Randomly choose the computer's move
    computer_choice = random.choice(choices)

    # Get the player's move
    user_choice=input('\nEnter your choice (stone, paper, scissor):').lower()

    # Check if the player's choice is valid
    if user_choice in choices:
        # Print the player's choice
        print("\nYou choseed " + user_choice)
        # Print the computer's choice
        print("\nComputer choseed " + computer_choice)
    else:
        print("\n Invalid input, choose a valid one")
        invalid_score += 1
        continue

    # Determine the winner of the round
    if (
        (user_choice == 'stone' and computer_choice == 'scissor') or
        (user_choice == 'paper' and computer_choice == 'stone') or
        (user_choice == 'scissor' and computer_choice == 'paper')
    ):
        print("\n You won")
        user_score += 1
    elif user_choice == computer_choice:
        print("\n It's a Tie")
        tied_score += 1
    else:
        print("\n Computer won")
        computer_score += 1

# Display the final score
print("\nFinal result:")
print("\n" + name + "'s score is " + str(user_score))
print("Computer's score is " + str(computer_score))
print("Tied score is " + str(tied_score))
print("Invalid output is " + str(invalid_score))

# Determine the overall winner of the game
if user_score > computer_score:
    print("\n Congratulations " + name + " you won this game")
elif user_score < computer_score:
    print("\n Computer won this game")
else:
    print("\nThe game is tied")

print("\n Well played, Thank You")
