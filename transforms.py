from re import search


def transform_program(text):
    """Transform the string into a list representing one operation of the program."""
    return [[y for y in x.split(" ")] for x in text if x]


def transform_register_string(text):
    """Transform the string into a list with each integer element."""
    reg = search(r".+\[(.+)\]", text)
    if reg:
        return [int(x) for x in reg.group(1).split(",")]
    raise ValueError


def transform_operation(text):
    """Transform the string into a list with each integer element."""
    return [int(x) for x in text.split(" ")]


def test_transform_register_string():
    """Verify that we can transform the string into the correct list."""
    assert transform_register_string("Before: [1, 0, 2, 0]") == [1, 0, 2, 0]
    assert transform_register_string("After:  [1, 1, 2, 0]") == [1, 1, 2, 0]


def test_transform_operation():
    """Verify that we can transform the string into the correct list."""
    assert transform_operation("4 1 0 1") == [4, 1, 0, 1]


def test_transform_program():
    """Verify that we can transform the string into the correct list."""
    assert transform_program(["", "9 3 3 0", "9 1 0 1"]) == [
        ["9", "3", "3", "0"],
        ["9", "1", "0", "1"],
    ]
