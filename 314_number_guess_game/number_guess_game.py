"""Game with functions to select a random target, give guess feedback, track turns"""
from random import randrange


class NumberGuessGame:
    """Class representing the game"""

    def __init__(self, player, max_val):
        self.player = player
        self.max_val = max_val
        self.turn_count = 0
        self.target_val = randrange(max_val)
        print(f"game started for {player}")

    def take_turn(self, guess: int):
        """Check if guess is correct, if not return higher/lower feedback"""
        self.turn_count += 1
        print(f"turn count {self.turn_count}")
        if guess == self.target_val:
            print(
                f"Congrats! You correctly guessed the target in {self.turn_count} turns"
            )
        if guess > self.target_val:
            print("lower")
        if guess < self.target_val:
            print("higher")

    def summarize(self):
        """Get game summary"""
        print(
            f"player {self.player} has taken {self.turn_count} turns trying to guess a value of {self.max_val} or less"
        )
