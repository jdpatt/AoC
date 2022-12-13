"""Day 6 AoC 2022"""


def get_marker(datastream, width=4):
    for index in range(len(datastream)):
        if len(set(datastream[index : index + width])) == width:
            return index + width


if __name__ == "__main__":

    #! Open and read in the puzzle. ----------------------------------------------
    with open("./2022/day_06_input.txt") as puzzle_input:
        datastream = puzzle_input.read()

    # ? Part 1  ----------------------------------------------
    packet_marker = get_marker(datastream)
    print(f"{packet_marker=}")

    # * Part 2  ----------------------------------------------
    message_marker = get_marker(datastream, 14)
    print(f"{message_marker=}")
