"""Day 5 AoC 2022"""
from copy import deepcopy
from collections import defaultdict
import re


def crate_mover_9000(stacks, quantity, source, destination):
    for _ in range(quantity):
        stacks[destination].append(stacks[source].pop())
    return stacks


def crate_mover_9001(stacks, quantity, source, destination):
    stacks[destination].extend(stacks[source][-quantity::])
    del stacks[source][-quantity::]  # pop multiple at once.
    return stacks


if __name__ == "__main__":

    #! Open and read in the puzzle. ----------------------------------------------
    starting_stack_config = defaultdict(list)
    with open("./2022/day_05_input.txt") as puzzle_input:
        for line in puzzle_input:
            if line == "\n":
                break
            for index, slice in enumerate(range(0, len(line), 4), start=1):
                character = line[slice + 1]  # Add the second character to the stack
                if character != " ":
                    starting_stack_config[index].insert(0, character)

        # Move "qty" from "source" to "destination"
        moves = [
            re.search(r"^[a-z ]+(\d+)[a-z ]+(\d+)[a-z ]+(\d+)", line).groups()
            for line in puzzle_input
        ]

    part_1_stacks = deepcopy(starting_stack_config)
    part_2_stacks = deepcopy(starting_stack_config)
    # ? Part 1  ----------------------------------------------
    for move in moves:
        part_1_stacks = crate_mover_9000(part_1_stacks, int(move[0]), int(move[1]), int(move[2]))

    characters = "".join([column[-1] for _, column in sorted(part_1_stacks.items())])
    print(f"Characters on the top with crate mover 9000: {characters}")

    # * Part 2  ----------------------------------------------
    for move in moves:
        part_2_stacks = crate_mover_9001(part_2_stacks, int(move[0]), int(move[1]), int(move[2]))
    characters = "".join([column[-1] for _, column in sorted(part_2_stacks.items())])
    print(f"Characters on the top with crate mover 9001: {characters}")
