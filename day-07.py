import os
import re
import math
from enum import Enum
from urllib import request
from dotenv import load_dotenv
from typing import Optional


load_dotenv()

input_url = 'https://adventofcode.com/2022/day/7/input'
headers = {
    'Authority': 'adventofcode.com',
    'cookie': f'session={os.getenv("COOKIE")}',
}
req = request.Request(input_url, headers=headers)


with request.urlopen(req) as res:
    NodeType = Enum('NodeType', 'DIR FILE')

    class Node:
        def __init__(self, name: str) -> None:
            self.name = name
            self.children = None
            self.parent = None
            self.size = 0

        def add_child(self, child):
            if self.children is None:
                self.children = []
            self.children.append(child)

        def set_size(self, size: int):
            self.size = size

        def set_parent(self, parent):
            self.parent = parent

        def get_type(self) -> NodeType:
            return NodeType.FILE if self.children is None else NodeType.DIR

        def get_size(self):
            if self.get_type() == NodeType.FILE:
                return self.size
            size = sum(child.get_size() for child in self.children)
            self.size = size # Memoize value
            return size


    # TODO: Read line-by-line to save memory
    all_input: str = res.read().decode('utf8')
    lines = all_input.split('\n')

    current_node: Optional[Node] = None
    root_node = None

    # Build directory tree
    for line in lines:
        if line.startswith('$ cd'):
            match = re.match('^\$ cd (.+)', line)
            dirname = match.group(1)
            if dirname == '..':
                current_node = current_node.parent
                continue
            new_node = Node(dirname)
            if dirname == '/':
                root_node = new_node
            if current_node is not None:
                current_node.add_child(new_node)
                new_node.set_parent(current_node)
            current_node = new_node
        elif line == '$ ls':
            pass
        else:
            match = re.match('^(\d+) (.+)', line)
            if match:
                size = int(match.group(1))
                file_name = match.group(2)
                new_node = Node(file_name)
                new_node.set_size(size)
                current_node.add_child(new_node)

    # Part 1
    # Small dirs have size <= 100,000
    def get_total_size_of_small_dirs(node) -> int:
        node_type = node.get_type()
        if node_type == NodeType.FILE:
            return 0

        total_size = 0

        node_size = node.get_size()
        if node_size <= 100_000:
            total_size += node_size

        for child in node.children:
            total_size += get_total_size_of_small_dirs(child)

        return total_size

    print(f'Total size of small dirs: {get_total_size_of_small_dirs(root_node)}')

    # Part 2
    TOTAL_DISK_SPACE = 70_000_000
    REQUIRED_DISK_SPACE = 30_000_000

    remaining_space = TOTAL_DISK_SPACE - root_node.get_size()
    minimum_space_to_free = REQUIRED_DISK_SPACE - remaining_space

    def find_minimum_directory_size_to_delete(min_size, node):
        node_type = node.get_type()
        if node_type == NodeType.FILE:
            return None

        min_dirsize = math.inf
        node_size = node.get_size()
        if node_size > min_size:
            min_dirsize = node_size
        for child in node.children:
            new_min_dirsize = find_minimum_directory_size_to_delete(min_size, child)
            if new_min_dirsize is not None:
                min_dirsize = min(min_dirsize, new_min_dirsize)
        return min_dirsize

    minimum_directory_size_to_delete = find_minimum_directory_size_to_delete(minimum_space_to_free, root_node)
    print(f'Minimum directory size to remove: {minimum_directory_size_to_delete}')
