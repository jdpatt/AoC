"""Advent of Code 2018 Day 3"""
from re import split


def find_conflicting_claims(array, width):
    """Sum all the incidents of 2 or more claims."""
    count = 0
    for row in range(width):
        for column in range(width):
            if len(array[row][column]) >= 2:
                count += 1
    return count


def is_overlapping(array, cord_x, cord_y, size_x, size_y):
    """Check the claim to see if it has any elements with more than one claim."""
    for x_offset in range(size_x):
        for y_offset in range(size_y):
            if len(array[cord_x + x_offset][cord_y + y_offset]) > 1:
                return True
    return False


def find_nonoverlapping_claim(array):
    """Find the one element with no overlapping claims."""
    with open("input/input3.txt", "r") as input_text:
        for line in input_text:
            tag_id, cord_x, cord_y, size_x, size_y = split(r" @ |,|: |x", line)
            if not is_overlapping(
                array, int(cord_x), int(cord_y), int(size_x), int(size_y)
            ):
                return tag_id
    raise ValueError("No Unique ID found.")


def generate_fabric_claims(width: int):
    """Generate the initial array based off the input of claims."""
    fabric = [[[] for x in range(width)] for i in range(width)]
    with open("input/input3.txt", "r") as input_text:
        for line in input_text:
            tag_id, cord_x, cord_y, size_x, size_y = split(r" @ |,|: |x", line)
            for x_offset in range(int(size_x)):
                for y_offset in range(int(size_y)):
                    fabric[int(cord_x) + x_offset][int(cord_y) + y_offset].append(
                        tag_id
                    )
    return fabric


if __name__ == "__main__":
    WIDTH = 1000
    FABRIC = generate_fabric_claims(WIDTH)
    CONFLICTS = find_conflicting_claims(FABRIC, WIDTH)
    print(f"Found {CONFLICTS} conflicting claims.")
    TAG_ID = find_nonoverlapping_claim(FABRIC)
    print(f"Non-overlapping Tag ID: {TAG_ID}")
