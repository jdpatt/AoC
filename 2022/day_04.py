"""Day 4 AoC 2022"""


def expand_to_list(string_range):
    """Take the string range and expand it into a list of numbers.

    Example:
        1-3 to [1, 2, 3]
    """
    lower, upper = string_range.split("-")
    return list(range(int(lower), int(upper) + 1))


def list_is_subset_of_list(sub_list, test_list):
    """If every element of the sub_list exists in test_list return True else False."""
    return all(x in test_list for x in sub_list)


def list_shares_items_with_list(compare_list, test_list):
    """If any element of the compare_list exists in test_list return True else False."""
    return any(x in test_list for x in compare_list)


if __name__ == "__main__":

    #! Open and read in the puzzle. ----------------------------------------------
    section_assignments = []
    with open("./2022/day_04_input.txt") as puzzle_input:
        for line in puzzle_input:
            elf_one_ranges, elf_two_ranges = line.strip().split(",")
            section_assignments.append(
                (expand_to_list(elf_one_ranges), expand_to_list(elf_two_ranges))
            )

    # ? Part 1  ----------------------------------------------
    subset_pairs = []
    for elf_one, elf_two in section_assignments:
        if list_is_subset_of_list(elf_one, elf_two) or list_is_subset_of_list(elf_two, elf_one):
            subset_pairs.append((elf_two, elf_two))

    print(f"Subset Pairs: {len(subset_pairs)}")

    # * Part 2  ----------------------------------------------
    overlapping_pairs = []
    for elf_one, elf_two in section_assignments:
        if list_shares_items_with_list(elf_one, elf_two) or list_shares_items_with_list(
            elf_two, elf_one
        ):
            overlapping_pairs.append((elf_two, elf_two))

    print(f"Overlapping Pairs: {len(overlapping_pairs)}")
