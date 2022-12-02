"""Day 1 AoC 2022"""
from itertools import groupby

with open("day_01_input.txt") as puzzle_input:
    calorie_listing = [
        list(map(int, group))
        for key, group in groupby([line.strip() for line in puzzle_input], key=bool)
        if key
    ]

total_calories_by_elf = sorted(
    [sum(elves_inventory) for elves_inventory in calorie_listing], reverse=True
)
print(f"The elf with the most calories has {max(total_calories_by_elf)} calories.")
print(f"The top three elves have a total of {sum(total_calories_by_elf[0:3])} calories.")
