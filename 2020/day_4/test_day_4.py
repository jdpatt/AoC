import pytest
from day_4 import PassPortValidator


@pytest.fixture
def validator():
    return PassPortValidator()


@pytest.mark.parametrize(
    "test",
    [
        "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",
        "eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
        "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
    ],
)
def test_valid_passports(test, validator):
    assert validator.is_valid_passport(test)


@pytest.mark.parametrize(
    "test",
    [
        "eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
        "iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946",
        "hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
        "hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007",
    ],
)
def test_invalid_passports(test, validator):
    assert not validator.is_valid_passport(test)


@pytest.mark.parametrize(
    "test",
    [
        ("byr", "1920"),
        ("byr", "2002"),
        ("iyr", "2010"),
        ("iyr", "2020"),
        ("eyr", "2020"),
        ("eyr", "2030"),
        ("hgt", "150cm"),
        ("hgt", "193cm"),
        ("hgt", "59in"),
        ("hgt", "76in"),
        ("hcl", "#888785"),
        ("hcl", "#88878f"),
        ("hcl", "#8abc85"),
        ("ecl", "amb"),
        ("ecl", "blu"),
        ("ecl", "brn"),
        ("pid", "166559648"),
        ("pid", "000559648"),
    ],
)
def test_valid_fields(test, validator):
    assert validator.is_valid_field(test[0], test[1])


@pytest.mark.parametrize(
    "test",
    [
        ("byr", "1919"),
        ("byr", "2003"),
        ("iyr", "2009"),
        ("iyr", "2021"),
        ("eyr", "2019"),
        ("eyr", "2031"),
        ("hgt", "149cm"),
        ("hgt", "194cm"),
        ("hgt", "58in"),
        ("hgt", "77in"),
        ("hcl", "#888j85"),
        ("hcl", "#85"),
        ("hcl", "#8888888888"),
        ("hcl", "#8abzcc85"),
        ("ecl", "blah"),
        ("ecl", "#blu"),
        ("ecl", "134in"),
        ("pid", "16655"),
        ("pid", "#blu"),
        ("pid", "134in"),
        ("pid", "166559abc"),
    ],
)
def test_invalid_fields(test, validator):
    assert not validator.is_valid_field(test[0], test[1])
