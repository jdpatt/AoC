"""Advent of Code 2018 Day 11"""

from common import get_puzzle_input


def calculate_fuel_cell(grid, serial):
    """Create the fuel cell and calculate each cell's value."""
    fuel_cell = []
    for row in range(1, grid + 1):
        fuel_row = []
        for column in range(1, grid + 1):
            fuel_row.append(calculate_power_level(column, row, serial))
        fuel_cell.append(fuel_row)
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


def find_max_sub_matrix(matrix, width, sub_width):
    """Find the largest sub matrix in the matrix."""
    sum_matrix = [[0] * width for _ in range(width)]


def main():
    """Main Puzzle Entry."""
    SERIAL_NUMBER = int(get_puzzle_input("input11.txt")[0])
    GRID_WIDTH = 6
    fuel_cell = calculate_fuel_cell(GRID_WIDTH, SERIAL_NUMBER)
    max_sub = find_max_sub_matrix(fuel_cell, GRID_WIDTH, 3)
    print(max_sub)


if __name__ == '__main__':
    main()


def test_calculate_power_level():
    assert calculate_power_level(3, 5, 8) == 4
    assert calculate_power_level(122, 79, 57) == -5
    assert calculate_power_level(217, 196, 39) == 0
    assert calculate_power_level(101, 153, 71) == 4
