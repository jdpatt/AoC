"""Help reduce clutter by moving common functions across puzzles to this module."""
from pathlib import Path


def get_input(filename):
    """Get the single line from the input file."""
    with open(Path().joinpath("input", filename), "r") as input_txt:
        return input_txt.read().splitlines()[0]


def get_and_transform_input(filename, transform=None):
    """Split and strip the trailing newlines from the input and optionally transform the input.

    If a function is passed to transform, this will run that function on every line of the input.
    """
    with open(Path().joinpath("input", filename), "r") as input_txt:
        if transform:
            return [transform(x) for x in input_txt.read().splitlines()]
        return input_txt.read().splitlines()
