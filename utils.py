# utils.py
# contains helper functions not directly relevant to the maze


def manhattan_distance(p1, p2):
    """
    Calculates the Manhattan distance between any two nodes.
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
