"""Advent of Code 2018 Day 9"""
from common import get_puzzle_input


def place_marble(marbles, current, new):
    pass

def play_marbles(players, last_marble):
    """Play a game of marbles with the elves."""
    scores = {player: 0 for player in range(players)}
    marbles = [0]
    current_marble = 1



if __name__ == "__main__":
    PUZZLE = get_puzzle_input("input9.txt")[0].split(" ")
    PLAYERS = int(PUZZLE[0])
    LAST_MARBLE = int(PUZZLE[6])
    print(PLAYERS)
    print(LAST_MARBLE)
