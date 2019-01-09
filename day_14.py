"""Advent of Code 2018 Day 14"""
from common import get_puzzle_input


def pick_new_recipe(current, scoreboard):
    """Pick the new recipe by adding 1 and the score of their current recipe."""
    moves = scoreboard[current] + 1
    return (current + moves) % len(scoreboard)


def create_new_recipe(scoreboard, elf1, elf2):
    """Create new recipes based off the sum of the two recipes."""
    new_recipes = str(scoreboard[elf1] + scoreboard[elf2])
    for letter in new_recipes:
        scoreboard.append(int(letter))
    elf1 = pick_new_recipe(elf1, scoreboard)
    elf2 = pick_new_recipe(elf2, scoreboard)
    return scoreboard, elf1, elf2


def main():
    """Main Puzzle Entry."""
    recipes = int(get_puzzle_input("input14.txt")[0])
    scoreboard = [3, 7]
    elf1 = 0  # The first elf picks the score at index 0
    elf2 = 1  # The second elf gets the next one
    print("Part 1:")
    while len(scoreboard) < recipes + 10:
        scoreboard, elf1, elf2 = create_new_recipe(scoreboard, elf1, elf2)
    print("".join([str(x) for x in scoreboard[-10:]]))
    print("Part 2:")


if __name__ == "__main__":
    main()


def test_create_new_recipes():
    """Verify that the example works."""
    assert create_new_recipe([3, 7], 0, 1) == ([3, 7, 1, 0], 0, 1)
    scoreboard = [3, 7]
    elf1 = 0
    elf2 = 1
    for _ in range(10):
        scoreboard, elf1, elf2 = create_new_recipe(scoreboard, elf1, elf2)
    assert scoreboard == [3, 7, 1, 0, 1, 0, 1, 2, 4, 5, 1, 5, 8, 9]


def test_pick_new_recipe():
    """Verify that we cycle through the scorecard correctly."""
    assert pick_new_recipe(0, [3, 7, 1, 0]) == 0
    assert pick_new_recipe(1, [3, 7, 1, 0]) == 1
    assert pick_new_recipe(2, [3, 7, 1, 0]) == 0
