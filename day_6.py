"""Advent of Code 2018 Day 6"""
from common import get_puzzle_input

if __name__ == "__main__":
    COORDINATES = [(int(x[0]), int(x[1])) for x in (x.split(",") for x in get_puzzle_input("input6.txt"))]
    print(COORDINATES)
