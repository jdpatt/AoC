"""Advent of Code 2018 Day 12"""
from typing import Sequence, Dict

from shared.common import get_puzzle_input


def transform_patterns(patterns: Sequence) -> Dict:
    """Transform the patterns from a string of `##... => .` to a usable pattern and result."""
    return {
        key.strip(): value.strip()
        for key, value in [pattern.split("=>") for pattern in patterns]
    }


def transform_initial_state(state: str):
    """Turn the initial string of pots into a dictionary who's index is the location of the pot."""
    starting_state = {-3: ".", -2: ".", -1: "."}
    for index, letter in enumerate(state):
        starting_state[index] = letter
    end_of_dict = max(starting_state) + 1
    for pot_on_end in range(end_of_dict, end_of_dict + 11):
        starting_state[pot_on_end] = "."
    return starting_state


def calculate_new_generation(current_gen: Dict, patterns: Dict) -> Dict:
    """Calculate the next generation based off the last generation and the patterns."""
    next_gen = {**current_gen}
    for pot, plant in current_gen.items():
        plant_string = "".join(
            [
                current_gen.get(pot - 2, "."),
                current_gen.get(pot - 1, "."),
                plant,
                current_gen.get(pot + 1, "."),
                current_gen.get(pot + 2, "."),
            ]
        )
        for pattern, result in patterns.items():
            if pattern == plant_string:
                next_gen[pot] = result
                break
            else:
                next_gen[pot] = "."
    return next_gen


def count_pots_with_plants(generation: Dict) -> int:
    """Sum any index that has a plant in it (#)."""
    plant_count = 0
    for pot_index, plant in generation.items():
        if plant == "#":
            plant_count += pot_index
    return plant_count


def get_more_pots(current_pots: Dict) -> Dict:
    """See that we have too many plants growing and add some more pots.

    Make sure that there is always five empty pots to the left and right if the lowest and highest
    pots are taken.
    """
    smallest = min(
        current_pots
    )  # Always should be negative due to initial state being 0.
    largest = max(current_pots)
    if current_pots[smallest] == "#":
        for pot in range(smallest - 1, smallest - 6, -1):
            current_pots[pot] = "."
    if current_pots[largest] == "#":
        for pot in range(largest + 1, largest + 6):
            current_pots[pot] = "."
    return current_pots


if __name__ == "__main__":
    PUZZLE = get_puzzle_input("input/input12.txt")
    GENERATIONS = 200  # After about 160 loops; every generation is adding 8.
    CURRENT_GEN = transform_initial_state(PUZZLE[0][15:])
    PATTERNS = transform_patterns(PUZZLE[2:])
    for loop in range(0, GENERATIONS):
        CURRENT_GEN = calculate_new_generation(CURRENT_GEN, PATTERNS)
        CURRENT_GEN = get_more_pots(CURRENT_GEN)
    COUNT = count_pots_with_plants(CURRENT_GEN)
    COUNT = COUNT + (50_000_000_000 - GENERATIONS) * 8
    print(f"Final Plant Count: {COUNT}")


def test_transform_initial_state():
    """Verify that the input string it correctly turned in to the expected dictionary."""
    results = transform_initial_state("#..#.#..##......###...###")
    assert (
        "".join(x for x in results.values())
        == "...#..#.#..##......###...###..........."
    )


def test_count_pots_with_plants():
    """Verify that count_pots_with_plants counts correctly."""
    assert count_pots_with_plants({0: "#", 1: "#", 2: ".", 3: "."}) == 1
    assert count_pots_with_plants({-5: "#", 1: "#", 2: ".", 3: "."}) == -4
    assert count_pots_with_plants({0: "#", 35: "#", 2: ".", 3: "."}) == 35


def test_calculate_new_generation():
    """Verify that calculate_new_generation calculates the next generation
    based off of the example.
    """
    patterns = {
        "...##": "#",
        "..#..": "#",
        ".#...": "#",
        ".#.#.": "#",
        ".#.##": "#",
        ".##..": "#",
        ".####": "#",
        "#.#.#": "#",
        "#.###": "#",
        "##.#.": "#",
        "##.##": "#",
        "###..": "#",
        "###.#": "#",
        "####.": "#",
    }
    first_gen = {
        -3: ".",
        -2: ".",
        -1: ".",
        0: "#",
        1: ".",
        2: ".",
        3: "#",
        4: ".",
        5: "#",
        6: ".",
        7: ".",
        8: "#",
        9: "#",
        10: ".",
        11: ".",
        12: ".",
        13: ".",
        14: ".",
        15: ".",
        16: "#",
        17: "#",
        18: "#",
        19: ".",
        20: ".",
        21: ".",
        22: "#",
        23: "#",
        24: "#",
        25: ".",
        26: ".",
        27: ".",
        28: ".",
        29: ".",
        30: ".",
        31: ".",
        32: ".",
        33: ".",
        34: ".",
        35: ".",
    }
    second_gen = calculate_new_generation(first_gen, patterns)
    assert (
        "".join(x for x in second_gen.values())
        == "...#...#....#.....#..#..#..#..........."
    )
    third_gen = calculate_new_generation(second_gen, patterns)
    assert (
        "".join(x for x in third_gen.values())
        == "...##..##...##....#..#..#..##.........."
    )


def test_get_more_pots():
    """Verify that we append and prepend pots correctly."""
    assert get_more_pots({-5: "#", 5: "#"}) == {
        -10: ".",
        -9: ".",
        -8: ".",
        -7: ".",
        -6: ".",
        -5: "#",
        5: "#",
        6: ".",
        7: ".",
        8: ".",
        9: ".",
        10: ".",
    }
