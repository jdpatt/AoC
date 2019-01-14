"""Advent of Code 2018 Day 5"""


def is_reactive(unit_a, unit_b):
    """If the units are reactive return true."""
    return unit_a == unit_b.swapcase()


def reduce_polymer(polymer):
    """Remove all reactive elements."""
    reduced = []
    for unit in polymer:
        if reduced and is_reactive(unit, reduced[-1]):
            reduced.pop()
        else:
            reduced.append(unit)
    return "".join(reduced)


def remove_letter(text, letter):
    """Remove both cases of the letter from the string."""
    text = text.replace(letter, "")
    text = text.replace(letter.swapcase(), "")
    return text


def optimize_polymer(polymer):
    """Removing one type of unit; see how small the polymer can get."""
    return min(
        [
            len(reduce_polymer(remove_letter(polymer, chr(x))))
            for x in range(ord("a"), (ord("z") + 1))
        ]
    )


if __name__ == "__main__":
    with open("input/input5.txt", "r") as input_txt:
        POLYMER = input_txt.read().strip()
    print(f"Original Length: {len(POLYMER)}")
    print(f"Reduced Length: {len(reduce_polymer(POLYMER))}")
    print(f"Optimized Length: {optimize_polymer(POLYMER)}")


def test_is_reactive():
    """Verify that swapcase works for all cases."""
    assert is_reactive("A", "a")
    assert is_reactive("a", "A")
    assert not is_reactive("A", "A")
    assert not is_reactive("a", "a")
    assert not is_reactive("A", "B")


def test_reduce_polymer():
    """Verify that we actually reduce the string."""
    assert reduce_polymer("aa") == "aa"
    assert reduce_polymer("aA") == ""
    assert reduce_polymer("aAa") == "a"
