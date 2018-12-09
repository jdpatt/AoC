"""Advent of Code 2018 Day 8"""
from common import get_puzzle_input


class Node(object):
    """Define what a node in the tree looks like."""

    def __init__(self, parent, meta):
        super(Node, self).__init__()
        self.parent = parent
        self.meta = meta


def generate_nodes(tree, data, parent):
    """Walk through the tree, recursively generating nodes"""
    node = Node(parent, [])
    num_of_children = next(data)
    num_of_metadata = next(data)
    for child in range(num_of_children):
        tree, data = generate_nodes(tree, data, node)
    for meta in range(num_of_metadata):
        node.meta.append(next(data))
    tree.append(node)
    return tree, data


if __name__ == '__main__':
    puzzle = [int(x) for x in get_puzzle_input("input8.txt")[0].split(" ")]
    tree, _ = generate_nodes([], iter(puzzle), "Root")
    print(f"Metadata sum: {sum([sum(node.meta) for node in tree])}")
