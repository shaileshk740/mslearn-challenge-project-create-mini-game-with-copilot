import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0

    def get_winner(self, player1_choice, player2_choice):
        if player1_choice == player2_choice:
            return "It's a tie!"
        elif (player1_choice == "rock" and player2_choice == "scissors") or \
             (player1_choice == "scissors" and player2_choice == "paper") or \
             (player1_choice == "paper" and player2_choice == "rock"):
            self.player_score += 1
            return "Player wins!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def play_round(self):
        while True:
            player_choice = input("Enter rock, paper, or scissors: ").lower()
            if player_choice not in self.choices:
                print("Invalid choice. Please try again.")
                continue
            break

        computer_choice = random.choice(self.choices)
        print(f"Computer chooses: {computer_choice}")
        result = self.get_winner(player_choice, computer_choice)
        print(result)

    def play_game(self):
        print("Welcome to Rock, Paper, Scissors!")
        while True:
            self.play_round()
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break
        print(f"Final Score - Player: {self.player_score}, Computer: {self.computer_score}")
        print("Thanks for playing!")

# Example usage
if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()