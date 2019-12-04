"""Advent of Code 2019 Day 3"""
import itertools

from shared.common import get_and_transform_input


def has_duplicate_and_adjacent(number):
    digits = [int(x) for x in str(number)]
    for index in range(len(digits) - 1):
        if digits[index] == digits[index + 1]:
            return True
    return False


def digits_never_decrease(number):
    digits = [int(x) for x in str(number)]
    for index in range(len(digits) - 1):
        if digits[index + 1] < digits[index]:
            return False
    return True


def duplicate_pairs_only(number):
    groups = [list(g) for _, g in itertools.groupby(str(number))]
    for group in groups:
        if len(group) == 2:
            return True
    return False


if __name__ == "__main__":
    PUZZLE = get_and_transform_input("input4.txt")[0]
    lower_bound, higher_bound = (int(x) for x in PUZZLE.split("-"))
    passwords = 0
    part2_passwords = 0
    for number in range(lower_bound, higher_bound + 1):
        if has_duplicate_and_adjacent(number) and digits_never_decrease(number):
            passwords += 1
        if duplicate_pairs_only(number) and digits_never_decrease(number):
            part2_passwords += 1
    print(f"Number of Valid Passwords for Part 1: {passwords}")
    print(f"Number of Valid Passwords for Part 2: {part2_passwords}")


def test_has_duplicate_and_adjacent():
    assert has_duplicate_and_adjacent(111111)
    assert has_duplicate_and_adjacent(223450)
    assert not has_duplicate_and_adjacent(123789)


def test_duplicate_pairs_only():
    assert duplicate_pairs_only(112233)
    assert not duplicate_pairs_only(123444)
    assert duplicate_pairs_only(111122)


def test_digits_never_decrease():
    assert digits_never_decrease(111111)
    assert not digits_never_decrease(223450)
    assert digits_never_decrease(123789)
