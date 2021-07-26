"""Puzzle Day 4"""
import re
from pathlib import Path


class PassPortValidator:
    def __init__(self) -> None:
        self._VALIDATORS = {
            "byr": self._birth_year,
            "iyr": self._issue_year,
            "eyr": self._expiration_year,
            "hgt": self._height,
            "hcl": self._hair_color,
            "ecl": self._eye_color,
            "pid": self._pid,
        }

    def has_required_fields(self, passport):
        return all(field in passport for field in self._VALIDATORS.keys())

    def is_valid_field(self, field, line):
        validator = self._VALIDATORS.get(field, None)
        if validator:
            return validator(line)
        return True

    def is_valid_passport(self, passport):
        """ "Prevent bad passports from getting past."""
        passport_fields = passport.strip().split(" ")
        for raw_data in passport_fields:
            field, value = raw_data.split(":")
            if not self.is_valid_field(field, value):
                return False
        return True

    def _birth_year(self, year):
        """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
        year = int(year)
        if 1920 <= year and year <= 2002:
            return True

    def _issue_year(self, year):
        """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""
        year = int(year)
        if 2010 <= year and year <= 2020:
            return True

    def _expiration_year(self, year):
        """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""
        year = int(year)
        if 2020 <= year and year <= 2030:
            return True

    def _height(self, height):
        """hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
        """
        if regex := re.match(r"(?P<value>\d+)(?P<units>cm|in)", height):
            value = int(regex.group("value"))
            if regex.group("units") == "cm":
                if 150 <= value and value <= 193:
                    return True
            else:
                if 59 <= value and value <= 76:
                    return True

    def _hair_color(self, color):
        """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."""
        if len(color) == 7 and re.match(r"#[a-f0-9]{6}", color):
            return True

    def _eye_color(self, color):
        """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
        if any(
            okay_color == color
            for okay_color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        ):
            return True

    def _pid(self, identification):
        """pid (Passport ID) - a nine-digit number, including leading zeroes."""
        if len(identification) == 9 and re.match(r"\d{9}", identification):
            return True


if __name__ == "__main__":
    with open(Path(__file__).parent.joinpath("input.txt")) as puzzle_input:
        passports = [
            group.replace("\n", " ") for group in puzzle_input.read().split("\n\n")
        ]

    checker = PassPortValidator()

    num_missing_cid = 0
    num_valid_passports = 0
    for passport in passports:
        if checker.has_required_fields(passport):
            num_missing_cid += 1
            if checker.is_valid_passport(passport):
                num_valid_passports += 1

    print(f"Missing cid (Part 1): {num_missing_cid}")  # 208
    print(f"Missing cid with Validated Data (Part 2): {num_valid_passports}")  # 167
