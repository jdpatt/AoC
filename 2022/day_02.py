"""Day 2 AoC 2022"""

from enum import Enum, IntEnum, auto


class Move(Enum):
    Rock = auto()
    Paper = auto()
    Scissors = auto()


class Score(IntEnum):
    Lose = 0
    Rock = 1
    Paper = 2
    Scissors = 3
    Draw = 3
    Win = 6


Moves = {
    "A": Move.Rock,
    "X": Move.Rock,
    "B": Move.Paper,
    "Y": Move.Paper,
    "C": Move.Scissors,
    "Z": Move.Scissors,
}

Outcomes = {"X": Score.Lose, "Y": Score.Draw, "Z": Score.Win}


def play_round(opponent: Move, my_move: Move):
    """Play rock, paper, scissors and return if we won/lost/tied the round."""
    if opponent == Move.Rock:
        if my_move == Move.Paper:
            return Score.Win
        if my_move == Move.Scissors:
            return Score.Lose
        return Score.Draw
    if opponent == Move.Paper:
        if my_move == Move.Paper:
            return Score.Draw
        if my_move == Move.Scissors:
            return Score.Win
        return Score.Lose
    if opponent == Move.Scissors:
        if my_move == Move.Paper:
            return Score.Lose
        if my_move == Move.Scissors:
            return Score.Draw
        return Score.Win


def score_of_winning_move(opponent: Move, results: Score):
    """Find the move that we must use to make the results equal."""
    for move in Moves.values():
        if play_round(opponent, move) == results:
            return Score[move.name]


def score_round_by_move(opponent, my_move):
    """Play rock, paper, scissors and score based on knowing the moves."""
    return play_round(opponent, my_move) + Score[my_move.name]


def score_round_by_outcome(opponent: Move, outcome: Outcomes):
    """Play rock, paper, scissors and score based on knowing the outcome."""
    return Score[outcome.name] + score_of_winning_move(opponent, outcome)


#! Open and read in the puzzle. ----------------------------------------------
with open("./day_02_input.txt") as puzzle_input:
    # Store every round into a dictionary of their move and my move.
    strategy_guide = [
        [moves[0], moves[1]] for moves in (line.strip().split(" ") for line in puzzle_input)
    ]


# ? Part 1  ----------------------------------------------
scores_by_move = [
    score_round_by_move(Moves.get(opponent), Moves.get(my_move))
    for opponent, my_move in strategy_guide
]

# * Part 2  ----------------------------------------------
scores_by_outcome = [
    score_round_by_outcome(Moves.get(opponent), Outcomes.get(outcome))
    for opponent, outcome in strategy_guide
]

# Sum and print the total
print(f"Total Score by Move: {sum(scores_by_move)}")
print(f"Total Score by Outcome: {sum(scores_by_outcome)}")
