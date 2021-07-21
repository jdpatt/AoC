"""Puzzle Day 2

1-3 a: abcde  (a must exist in the string one to three times to be valid)
1-3 b: cdefg
2-9 c: ccccccccc

"""
from pathlib import Path


def is_valid_password_for_sled_rental(string):
    string = string.replace(":", "")
    amount, letter, password = string.split(" ")
    lower, upper = [int(x) for x in amount.split("-")]
    if lower <= password.count(letter) <= upper:
        return True


def is_valid_password_for_toboggan(string):
    string = string.replace(":", "")
    amount, letter, password = string.split(" ")
    position_one, position_two = [int(x) for x in amount.split("-")]
    if bool(password[position_one - 1] == letter) ^ bool(
        password[position_two - 1] == letter
    ):
        return True


if __name__ == "__main__":
    with open(Path(__file__).parent.joinpath("input.txt")) as puzzle_input:
        passwords_and_policy = puzzle_input.readlines()
    valid_password_count = 0
    for item in passwords_and_policy:
        if is_valid_password_for_sled_rental(item):
            valid_password_count += 1
    print(f"Valid Sled Passwords: {valid_password_count}")
    # Valid Sled Passwords: 396
    valid_password_count = 0
    for item in passwords_and_policy:
        if is_valid_password_for_toboggan(item):
            valid_password_count += 1
    print(f"Valid Toboggan Passwords: {valid_password_count}")
    # Valid Toboggan Passwords: 428
