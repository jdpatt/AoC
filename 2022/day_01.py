"""Day 1 AoC 2022"""
from itertools import groupby

if __name__ == "__main__":

    with open("./day_01_input.txt") as puzzle_input:
        all_elves_calories = [
            # convert all the string numbers to ints
            list(map(int, group))
            # break up the lists by where they are empty or not with bool(item_to_check)
            for key, group in groupby([line.strip() for line in puzzle_input], key=bool)
            # if the group is empty or only one blank, skip it.
            if key
        ]

    total_calories_by_elf = sorted(
        [sum(elf_calories) for elf_calories in all_elves_calories], reverse=True
    )
    print(f"The elf with the most calories has {max(total_calories_by_elf)} calories.")
    print(f"The top three elves have a total of {sum(total_calories_by_elf[0:3])} calories.")
