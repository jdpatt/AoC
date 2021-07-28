"""day 5"""
from pathlib import Path
from typing import List


def get_seat_id(row: int, column: int):
    return (row * 8) + column


def down_select_seats(iterable: List[int], character: str):
    """If the character is F or L, return the lower half of the list."""
    if character == "F" or character == "L":
        return iterable[: len(iterable) // 2]
    return iterable[len(iterable) // 2 :]


def find_your_seat(seats):
    seats = sorted(seats)
    return list(set(range(seats[0], seats[-1] + 1)) - set(seats))[0]


if __name__ == "__main__":
    with open(Path(__file__).parent.joinpath("input.txt")) as puzzle_input:
        boarding_passes = puzzle_input.readlines()
    seat_ids = list()
    for boarding_pass in boarding_passes:
        rows = list(range(128))
        columns = list(range(8))
        for index, character in enumerate(boarding_pass):
            if index < 7:
                rows = down_select_seats(rows, character)
            else:
                columns = down_select_seats(columns, character)
        seat_ids.append(get_seat_id(rows[0], columns[0]))
    print(f"Highest Seat ID Found (Part 1): {max(seat_ids)}")  # 871
    print(f"Your Seat is: {find_your_seat(seat_ids)}")  # 640
