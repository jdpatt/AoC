"""Help reduce clutter by moving common functions across puzzles to this module."""


def get_puzzle_input(filename):
    """Split and strip the trailing newlines from the input."""
    with open(filename, "r") as input_txt:
        puzzle = input_txt.read().splitlines()
        return puzzle
