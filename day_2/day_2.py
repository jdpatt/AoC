"""Advent of Code 2018 Day 2"""
from collections import defaultdict
from difflib import SequenceMatcher
from typing import Sequence, Dict


def has_repeating_characters(characters: Dict, num_repeating: int):
    """Search a string for num_repeating characters."""
    for _, value in characters.items():
        if value == num_repeating:
            return True
    return False


def generate_checksum(potential_ids: Sequence[str]):
    """Sum the total number of strings containing two or three repeating letters, then multiply."""
    two_chars = 0
    three_chars = 0
    for item in potential_ids:
        charcter_count = defaultdict(int)
        for letter in item:
            charcter_count[letter] += 1
        if has_repeating_characters(charcter_count, num_repeating=2):
            two_chars += 1
        if has_repeating_characters(charcter_count, num_repeating=3):
            three_chars += 1
    return two_chars * three_chars


def find_fabric_ids(potential_ids: Sequence[str]):
    """Find the two ids that are only off by one character."""
    ratio = (len(potential_ids[0]) - 1) / len(potential_ids[0])
    for item_one in potential_ids:
        for item_two in potential_ids:
            seq = SequenceMatcher(None, item_one, item_two)
            if seq.ratio() >= ratio and seq.ratio() != 1:
                matches = seq.get_matching_blocks()
                before = item_one[matches[0].a: matches[0].a + matches[0].size]
                after = item_one[matches[1].a: matches[1].a + matches[1].size]
                print(f"Common between the two IDs: {before}{after}")
                return


if __name__ == "__main__":
    with open("input.txt", "r") as input_text:
        IDS = input_text.readlines()
    print(f"Checksum: {generate_checksum(IDS)}")
    find_fabric_ids(IDS)
