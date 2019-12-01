"""Advent of Code 2018 Day 1"""

from shared.common import get_and_transform_input


def calc_fuel_for_mass(mass):
    """Fuel required to launch a given module is based on its mass.

    Specifically, to find the fuel required for a module, take its mass, divide by three,
    round down, and subtract 2.
    """
    return (mass // 3) - 2


def calc_total_fuel(mass):
    """Fuel itself requires fuel just like a module.

    take its mass, divide by three, round down, and subtract 2. However, that fuel also requires
    fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should
    instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled
    by wishing really hard, which has no mass and is outside the scope of this calculation.
    """
    total_fuel = 0
    fuel = calc_fuel_for_mass(mass)
    while fuel >= 0:
        total_fuel += fuel
        fuel = calc_fuel_for_mass(fuel)
    return total_fuel


if __name__ == "__main__":
    PUZZLE = get_and_transform_input("input1.txt", int)
    print(f"Part 1: {sum([calc_fuel_for_mass(mass) for mass in PUZZLE])}")
    print(f"Part 2: {sum([calc_total_fuel(mass) for mass in PUZZLE])}")


def test_calculate_fuel_for_mass():
    assert calc_fuel_for_mass(12) == 2
    assert calc_fuel_for_mass(14) == 2
    assert calc_fuel_for_mass(1969) == 654
    assert calc_fuel_for_mass(100756) == 33583


def test_calc_for_total_fuel():
    assert calc_total_fuel(14) == 2
    assert calc_total_fuel(1969) == 966
