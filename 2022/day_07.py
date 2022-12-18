"""Day 7 AoC 2022"""
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class FilesystemObject:
    name: str
    parent: "FilesystemObject" = None
    path: str = field(init=False)
    children: list = field(default_factory=list)
    is_dir: bool = False
    _current_index: int = 0
    size: int = 0

    def __post_init__(self):
        parent = self.parent
        if not parent:
            self.path = self.name
        else:
            parts = []
            while parent:
                parts.insert(0, parent.name)
                parent = parent.parent
            self.path = f"{'.'.join(parts)}.{self.name}"

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_item = self.children[self._current_index]
        except IndexError:
            self._current_index = 0
            raise StopIteration
        self._current_index += 1
        return next_item

    def add_item(self, item):
        if self.is_dir:
            self.children.append(item)

    def get_item(self, name):
        for item in self.children:
            if item.name == name:
                return item


def parse_filesystem(history):
    root = FilesystemObject("/", is_dir=True)
    current_dir = root
    for item in history:
        if "$ cd" in item:
            _, _, dir = item.split(" ")
            if dir == "/":
                current_dir = root
            elif dir == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.get_item(dir)
        elif "$ ls" in item:
            pass
        elif "dir" in item:
            _, name = item.split(" ")
            current_dir.add_item(FilesystemObject(name, parent=current_dir, is_dir=True, size=0))
        else:  # should be a file listing of size and name.
            size, name = item.split(" ")
            current_dir.add_item(
                FilesystemObject(name, parent=current_dir, is_dir=False, size=int(size))
            )
    return root


def directory_sizes(fileobject, dir_sizes):
    """Walk the filesystem tree and flatten out the directories."""
    for item in fileobject:
        if not item.is_dir:
            dir_sizes[fileobject.path] += item.size
        else:
            sub_dir_sizes = directory_sizes(item, defaultdict(int))
            for path, size in sub_dir_sizes.items():
                if fileobject.name == "/" and len(path.split(".")) > 2:
                    pass
                else:
                    dir_sizes[fileobject.path] += size
                dir_sizes[path] = size
    return dir_sizes


if __name__ == "__main__":

    #! Open and read in the puzzle. ----------------------------------------------
    with open("./2022/day_07_input.txt") as puzzle_input:
        # with open("./2022/example.txt") as puzzle_input:
        prompt_history = [item.strip() for item in puzzle_input.readlines()]

    filesystem = parse_filesystem(prompt_history)
    dir_sizes = directory_sizes(filesystem, defaultdict(int))

    # ? Part 1  ----------------------------------------------
    print(f"Part 1: {sum([size for size in dir_sizes.values() if size <= 100_000])}")
    print(f"Total Space: {dir_sizes['/']}")

    # * Part 2  ----------------------------------------------
    total_space = 70_000_000
    update_size = 30_000_000
    unused_space = total_space - dir_sizes["/"]
    print(f"Unused Space: {unused_space}")
    delete_candidates = {
        name: size for name, size in dir_sizes.items() if size + unused_space >= update_size
    }
    print(f"Part 2: {min(delete_candidates, key=delete_candidates.get)}")
