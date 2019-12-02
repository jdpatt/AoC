from day_1 import calc_fuel_for_mass, calc_total_fuel


def test_calculate_fuel_for_mass():
    assert calc_fuel_for_mass(12) == 2
    assert calc_fuel_for_mass(14) == 2
    assert calc_fuel_for_mass(1969) == 654
    assert calc_fuel_for_mass(100756) == 33583


def test_calc_for_total_fuel():
    assert calc_total_fuel(14) == 2
    assert calc_total_fuel(1969) == 966
