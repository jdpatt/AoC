"""Advent of Code 2018 Day 14"""
from itertools import cycle

from common import get_puzzle_input


def pick_new_recipe(score_index, scoreboard):
    """Pick the new recipe by adding 1 and the score of their current recipe"""
    scores = cycle(enumerate(scoreboard))
    score = next(scores)
    for _ in range(score_index):
        score = next(scores)
    move = int(score[1]) + 1
    for _ in range(move):
        score = next(scores)
    return score[0]


def create_new_recipe(scoreboard, elf1, elf2):
    """Create new recipes based off the sum of the two recipes."""
    new_recipes = str(int(scoreboard[elf1]) + int(scoreboard[elf2]))
    scoreboard = scoreboard + new_recipes
    elf1 = pick_new_recipe(elf1, scoreboard)
    elf2 = pick_new_recipe(elf2, scoreboard)
    return scoreboard, elf1, elf2


def main():
    """Main Puzzle Entry."""
    RECIPES = int(get_puzzle_input("input14.txt")[0])
    scoreboard = "37"
    elf1 = 0  # The first elf picks the score at index 0
    elf2 = 1  # The second elf gets the next one
    for loop in range(RECIPES):
        scoreboard, elf1, elf2 = create_new_recipe(scoreboard, elf1, elf2)
    print(scoreboard)
    length = len(scoreboard)
    while len(scoreboard) <= length + 10:
        scoreboard, elf1, elf2 = create_new_recipe(scoreboard, elf1, elf2)
    print(scoreboard)


if __name__ == "__main__":
    main()


def test_create_new_recipes():
    """Verify that the example works."""
    assert create_new_recipe("37", 0, 1) == ("3710", 0, 1)
    scoreboard = "37"
    elf1 = 0
    elf2 = 1
    for _ in range(10):
        scoreboard, elf1, elf2 = create_new_recipe(scoreboard, elf1, elf2)
    assert scoreboard == "37101012451589"


def test_pick_new_recipe():
    """Verify that we cycle through the scorecard correctly."""
    assert pick_new_recipe(0, "3710") == 0
    assert pick_new_recipe(1, "3710") == 1
