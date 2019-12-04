"""Advent of Code 2018 Day 14"""
import pytest

from shared.common import get_puzzle_input


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


def find_sub_list(main_list, sub_list):
    """Given a list find a sub list in it. If found return the index of the first match."""
    occurences = [i for i, x in enumerate(main_list) if x == sub_list[0]]
    for match in occurences:
        if sub_list == main_list[match : match + len(sub_list)]:
            return match
    raise ValueError


def main():
    """Main Puzzle Entry."""
    recipes = int(get_puzzle_input("input/input14.txt")[0])
    scoreboard = [3, 7]
    elf1 = 0  # The first elf picks the score at index 0
    elf2 = 1  # The second elf gets the next one
    print("Part 1:  Return 10 Recipes after number of iterations from puzzle input.")
    while len(scoreboard) < recipes + 10:
        scoreboard, elf1, elf2 = create_new_recipe(scoreboard, elf1, elf2)
    print("".join([str(x) for x in scoreboard[-10:]]))

    print("Part 2:  Return index of pattern match from puzzle input.")
    scoreboard = [3, 7]
    elf1 = 0  # The first elf picks the score at index 0
    elf2 = 1  # The second elf gets the next one
    pattern = [int(letter) for letter in str(recipes)]
    while True:
        scoreboard, elf1, elf2 = create_new_recipe(scoreboard, elf1, elf2)
        try:
            index = find_sub_list(scoreboard[-20:], pattern)
            if index:
                length = len(scoreboard) - (20 - index)
                print(f"Pattern Appears at {length}")
                print(scoreboard[-20:])
                break
        except ValueError:
            pass


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


def test_find_sub_list():
    """Verify that we can find a sublist in a given list and find the first match."""
    assert find_sub_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 6]) == 4
    assert find_sub_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 6, 7]) == 4
    with pytest.raises(ValueError):
        find_sub_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [6, 5])
