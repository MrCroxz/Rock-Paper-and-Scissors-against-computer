import random
import time

def get_user_choice(choices):
    """Gets and validates user input."""
    while True:
        user_choice = input(f"Choose among {', '.join(choices)} (or type 'q' to quit): ").lower()
        if user_choice in choices or user_choice == 'q':
            return user_choice
        print("Invalid choice, please try again!")

def decide_winner(user_choice, computer_choice, win_conditions):
    """Decides the winner based on the choices and winning conditions."""
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice, computer_choice) in win_conditions:
        return "user"
    else:
        return "computer"

def rock_paper_scissors():
    """Main function for Rock, Paper, Scissors game."""
    choices = ["rock", "paper", "scissors"]
    win_conditions = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}
    user_score = 0
    computer_score = 0

    print("\nWelcome to Rock, Paper, Scissors!\n")
    time.sleep(1)

    rounds = input("How many rounds would you like to play? (Press Enter for unlimited): ").strip()
    rounds = int(rounds) if rounds.isdigit() else None

    round_number = 0

    while rounds is None or round_number < rounds:
        round_number += 1
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice(choices)

        if user_choice == 'q':
            print("\nExiting the game. Thanks for playing!")
            break

        computer_choice = random.choice(choices)
        print(f"You chose: {user_choice}")
        time.sleep(0.5)
        print(f"Computer chose: {computer_choice}")

        winner = decide_winner(user_choice, computer_choice, win_conditions)

        if winner == "draw":
            print("It's a draw!")
        elif winner == "user":
            print("You won this round!")
            user_score += 1
        else:
            print("The computer won this round!")
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer\n")

        if rounds and round_number == rounds:
            print("The game is over!")
            break

    # Final message
    if user_score > computer_score:
        print("\nCongratulations! You won the game! 🎉")
    elif user_score < computer_score:
        print("\nThe computer won the game. Better luck next time! 🤖")
    else:
        print("\nIt's a tie! 🏳️")

    print(f"Final Score: You {user_score} - {computer_score} Computer")
    print("Thanks for playing!")

if __name__ == "__main__":
    rock_paper_scissors()
