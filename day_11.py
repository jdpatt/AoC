"""Advent of Code 2018 Day 11"""
# pylint: disable=C0103
# x, y and k are valid names for this puzzle.
from common import get_puzzle_input


def calculate_fuel_cell(grid_width, serial):
    """Create the fuel cell and calculate each cell's value.

    In X,Y notation, the top-left cell is 1,1, and the top-right cell is 300,1
    """
    fuel_cell = {}
    for row in range(1, grid_width + 1):
        for column in range(1, grid_width + 1):
            fuel_cell[(column, row)] = calculate_power_level(column, row, serial)
    return fuel_cell


def calculate_power_level(x, y, serial):
    """Calculate the current cell's power level."""
    rack_id = x + 10
    power_level = ((rack_id * y) + serial) * rack_id
    try:
        hundreds = int(str(power_level)[-3])
    except IndexError:
        hundreds = 0
    return hundreds - 5


def summed_area_table(matrix):
    """Compute the summed area table of the matrix.

    The summed area for any point is I(x,y) = i(x,y) + I(x, y - 1) + I(x - 1,y) - I(x - 1, y - 1)
    https://en.wikipedia.org/wiki/Summed-area_table
    """
    summed_table = {}
    for key, value in matrix.items():
        summed_table[key] = (
            value
            + summed_table.get((key[0], key[1] - 1), 0)
            + summed_table.get((key[0] - 1, key[1]), 0)
            - summed_table.get((key[0] - 1, key[1] - 1), 0)
        )
    return summed_table


def get_largest_sub_matrix(matrix, matrix_width, k):
    """Get the largest sub matrix of size of `k`."""
    largest = -100
    location = None
    for key, _ in matrix.items():
        if key[0] >= matrix_width - 1 or key[1] >= matrix_width - 1:
            pass
        else:
            sub_sum = get_sub_matrix_sum(matrix, key, k)
            if sub_sum > largest:
                largest = sub_sum
                location = key
    return largest, location


def get_sub_matrix_sum(matrix, start, k):
    """Return a sub matrix with the size of `k` starting at `start`.

    The sum of a sub matrix who's size of `k` is calculated by adding and subtracting points in
    the summed area table.  i(x,y) = I(D) + I(A) - I(B) - I(C) where A, B, C and D are the outer
    points of the rectangle.
    """
    k = k - 1  # Include in the start value in k
    point_a = matrix.get(start, 0)
    point_b = matrix.get((start[0], start[1] + k), 0)
    point_c = matrix.get((start[0] + k, start[1]), 0)
    point_d = matrix.get((start[0] + k, start[1] + k), 0)
    if start[0] == 1 and start[1] == 1:
        sum_sub = point_d
    else:
        sum_sub = point_a + point_d - point_b - point_c
    return sum_sub


def main():
    """Main Puzzle Entry."""
    SERIAL_NUMBER = int(get_puzzle_input("input11.txt")[0])
    GRID_WIDTH = 300
    fuel_cell = calculate_fuel_cell(GRID_WIDTH, SERIAL_NUMBER)
    max_sub = summed_area_table(fuel_cell)
    largest, location = get_largest_sub_matrix(max_sub, GRID_WIDTH, 3)
    print(fuel_cell)
    print(f"Top Left: {location} Largest: {largest}")


if __name__ == "__main__":
    main()


def test_calculate_power_level():
    assert calculate_power_level(3, 5, 8) == 4
    assert calculate_power_level(122, 79, 57) == -5
    assert calculate_power_level(217, 196, 39) == 0
    assert calculate_power_level(101, 153, 71) == 4


def test_summed_area_table():
    table = {}
    for row in range(1, 4):
        for column in range(1, 4):
            table[(row, column)] = column
    matrix = summed_area_table(table)
    assert matrix == {
        (1, 1): 1,
        (1, 2): 3,
        (1, 3): 6,
        (2, 1): 2,
        (2, 2): 6,
        (2, 3): 12,
        (3, 1): 3,
        (3, 2): 9,
        (3, 3): 18,
    }


def test_get_sub_matrix_sum():
    matrix = {
        (1, 1): 1,
        (1, 2): 3,
        (1, 3): 6,
        (2, 1): 2,
        (2, 2): 6,
        (2, 3): 12,
        (3, 1): 3,
        (3, 2): 9,
        (3, 3): 18,
    }
    assert get_sub_matrix_sum(matrix, (1, 1), 2) == 6
    assert get_sub_matrix_sum(matrix, (2, 2), 2) == 3
    assert get_sub_matrix_sum(matrix, (1, 1), 3) == 18
    assert get_sub_matrix_sum(matrix, (1, 1), 1) == 1


def test_get_largest_sub_matrix_example1():
    """For grid serial number 18, the largest total 3x3 square has a top-left corner of 33,45
    (with a total power of 29)"""
    max_sub = summed_area_table(calculate_fuel_cell(300, 18))
    largest, location = get_largest_sub_matrix(max_sub, 300, 3)
    assert location == (33, 45)
    assert largest == 29


def test_get_largest_sub_matrix_example2():
    """For grid serial number 42, the largest 3x3 square's top-left is 21,61
    (with a total power of 30)"""
    max_sub = summed_area_table(calculate_fuel_cell(300, 42))
    largest, location = get_largest_sub_matrix(max_sub, 300, 3)
    assert location == (21, 61)
    assert largest == 30
