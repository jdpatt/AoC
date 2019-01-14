"""Advent of Code 2018 Day 8"""
from shared.common import get_puzzle_input


class Node:
    """Define what a node in the tree looks like."""

    # pylint: disable=R0903

    def __init__(self, parent):
        super(Node, self).__init__()
        self.parent = parent
        self.meta = []
        self.child_values = []
        self.value = 0


def generate_nodes(tree, data, parent):
    """Walk through the tree, recursively generating nodes"""
    node = Node(parent)
    num_of_children = next(data)
    num_of_metadata = next(data)
    for _ in range(num_of_children):
        tree, data, val = generate_nodes(tree, data, node)
        node.child_values.append(val)
    for _ in range(num_of_metadata):
        node.meta.append(next(data))
    if num_of_children == 0:
        node.value = sum(node.meta)
    else:
        for val in node.meta:
            try:
                node.value += node.child_values[val - 1]
            except IndexError:
                pass
    tree.append(node)
    return tree, data, node.value


if __name__ == "__main__":
    PUZZLE = [int(x) for x in get_puzzle_input("input/input8.txt")[0].split(" ")]
    TREE, _, ROOT_VALUE = generate_nodes([], iter(PUZZLE), "Root")
    print(f"Metadata sum: {sum([sum(node.meta) for node in TREE])}")
    print(f"Root Value: {ROOT_VALUE}")
