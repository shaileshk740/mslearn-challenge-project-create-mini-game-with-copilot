import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

    def get_winner(self, player1_choice, player2_choice):
        if player1_choice == player2_choice:
            return "It's a tie!"
        elif (player1_choice == "rock" and player2_choice == "scissors") or \
             (player1_choice == "scissors" and player2_choice == "paper") or \
             (player1_choice == "paper" and player2_choice == "rock"):
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"

    def play_round(self):
        player1_choice = random.choice(self.choices)
        player2_choice = random.choice(self.choices)
        print(f"Player 1 chooses: {player1_choice}")
        print(f"Player 2 chooses: {player2_choice}")
        result = self.get_winner(player1_choice, player2_choice)
        print(result)

# Example usage
if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_round()