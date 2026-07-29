import random

print("=" * 50)
print("      ROCK PAPER SCISSORS GAME")
print("=" * 50)

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:

    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("Invalid Choice! Please enter rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print("\nYour Choice:", user_choice)
    print("Computer Choice:", computer_choice)

    if user_choice == computer_choice:
        print("\nIt's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("\nCongratulations! You Win!")
        user_score += 1

    else:
        print("\nComputer Wins!")
        computer_score += 1

    print("\nCurrent Score")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\n" + "=" * 50)
print("            FINAL SCORE")
print("=" * 50)

print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("\nOverall Winner: You")
elif computer_score > user_score:
    print("\nOverall Winner: Computer")
else:
    print("\nOverall Result: Match Tied")

print("\nThank You For Playing!")