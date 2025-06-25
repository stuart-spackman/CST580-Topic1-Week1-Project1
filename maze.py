# maze.py
# defines the maze, node class, and helper functions for search

# constants for readability
WAll = "#"
EMPTY = "."
START = "S"
TREASURE = "T"


def generate_maze():
    """Returns a hardcoded 2D list representing the maze grid."""
    maze = [
        ["S", ".", ".", "#", ".", ".", "."],
        ["#", "#", ".", "#", ".", "#", "."],
        [".", ".", ".", ".", ".", "#", "."],
        [".", "#", "#", "#", ".", "#", "."],
        [".", ".", ".", "#", ".", ".", "T"],
    ]

    return maze


def get_neighbors():
    """
    Given a position (row, col) and the maze,
    returns a list of valid neighboring positions (up, down, left, right)
    that are not walls and are within bounds.
    """


class Node:
    def __init__(self, position, parent=None, cost=0):
        self.position = position  # (row, col)
        self.parent = parent
        self.cost = cost  # CSF(n)

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)
