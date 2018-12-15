"""Advent of Code 2018 Day 9"""
from common import get_puzzle_input
from itertools import cycle


class Marble():
    """Circular Doubly Linked List"""

    def __init__(self, number, before=None, after=None):
        super(Marble, self).__init__()
        self.number = number
        self.previous = before
        self.next = after

    def remove(self):
        current_marble = self.next
        self.previous.next = self.next
        self.next.previous = self.previous
        return current_marble

    def append(self, number):
        marble = Marble(number, self, self.next)
        self.next.previous = marble
        self.next = marble
        return marble

    def __str__(self):
        return f"Marble: {self.number} Next: {self.next.number} Previous: {self.previous.number}"


def play_marbles(num_of_players, num_of_marbles):
    """Play a game of marbles with the elves."""
    player = cycle([x for x in range(num_of_players)])
    score = {key: 0 for key in range(num_of_players)}
    current_marble = Marble(0)
    current_marble.next = current_marble
    current_marble.previous = current_marble
    for marble, current_player in zip(range(1, num_of_marbles + 1), player):
        if marble % 23 == 0:
            score[current_player] += marble
            for _ in range(7):
                current_marble = current_marble.previous
            score[current_player] += current_marble.number
            current_marble = current_marble.remove()
        else:
            current_marble = current_marble.next.append(marble)
    return max(value for _, value in score.items())


if __name__ == "__main__":
    PUZZLE = get_puzzle_input("input9.txt")[0].split(" ")
    PLAYERS = int(PUZZLE[0])
    LAST_MARBLE = int(PUZZLE[6])
    FINAL_SCORE = play_marbles(PLAYERS, LAST_MARBLE)
    # print(f"32: {play_marbles(9, 25)}")
    # print(f"8317: {play_marbles(10, 1618)}")
    # print(f"146373: {play_marbles(13, 7999)}")
    # print(f"2764: {play_marbles(17, 1104)}")
    print(f"Final Score is {FINAL_SCORE}")
    print(f"Jackpot is {play_marbles(PLAYERS, LAST_MARBLE * 100)}")
