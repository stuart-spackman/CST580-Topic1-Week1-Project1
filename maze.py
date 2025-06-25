# maze.py
# defines the maze, node class, and helper functions for search

# constants for readability
WALL = "#"
EMPTY = "."
START = "S"
TREASURE = "T"


def generate_small_maze():
    """Returns a hardcoded 10x10 maze grid."""
    maze = [
        list("S.#.#####."),
        list(".#.#.....#"),
        list(".#.#.###.#"),
        list(".#...#...#"),
        list("###.#.###."),
        list("#...#...#."),
        list("#.#####.#."),
        list("#.......#."),
        list(".#######.#"),
        list("....#...T."),
    ]
    return maze


def generate_medium_maze():
    """Returns a hardcoded 2D list representing the maze grid."""
    maze = [
        list("S.#............."),
        list("#.#.#####.#####."),
        list("#.#.....#.....#."),
        list("#.#####.#.###.#."),
        list("#.....#.#.#.#.#."),
        list("#####.#.#.#.#.#."),
        list("#.....#.#.#.#.#."),
        list("#.#####.#.#.#.#."),
        list("#.......#.#.#.#."),
        list("#######.#.#.#.#."),
        list("#.......#.#.#.#."),
        list("#.#######.#.#.#."),
        list("#.........#...#."),
        list("###########.###."),
        list(".............T.."),
    ]

    return maze


def generate_maze():
    """Returns a hardcoded 20x20 maze grid."""
    maze = [
        list("S..##..#...###.....#."),
        list("##..#.#.#.#...#.#.#.#"),
        list("#....#.#.#.#.#.#.#..#"),
        list("#.####.#.#.#.#.#.##.#"),
        list("#.#....#...#.#.#....#"),
        list("#.#.#########.#.####."),
        list("#.#.........#.#.....#"),
        list("#.#########.#.#####.#"),
        list("#...........#.......#"),
        list("#####.###########.###"),
        list("#.....#.........#...#"),
        list("#.###.#.#######.#.###"),
        list("#...#.#.....#...#...#"),
        list("###.#.#####.#.###.#.#"),
        list("#...#.......#.....#.#"),
        list("#.###########.#####.#"),
        list("#.................#.#"),
        list("#.###############.#.#"),
        list("#.................#T#"),
        list("#####################"),
    ]
    return maze


def get_neighbors(position, maze):
    """
    Given a position (row, col) and the maze,
    returns a list of valid neighboring positions (up, down, left, right)
    that are not walls and are within bounds.
    """
    neighbors = []
    row, col = position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    rows = len(maze)
    cols = len(maze[0])

    for row_dir, col_dir in directions:
        r, c = row + row_dir, col + col_dir
        # check bounds and wall
        if 0 <= r < rows and 0 <= c < cols and maze[r][c] != WALL:
            neighbors.append((r, c))

    return neighbors


def reconstruct_path(end_node):
    """
    Reconstructs the path from start to goal using the parent links in nodes.
    Returns a list of positions (in the form of tuples) representing the path.
    """
    path = []
    current = end_node
    while current:
        path.append(current.position)
        current = current.parent
    path.reverse()

    return path


class Node:
    """
    Node class used by search algorithms to represetn states in the maze.
    Tracks position, parent (for path reconstruction), and optional cost.
    """

    def __init__(self, position, parent=None, cost=0):
        self.position = position  # (row, col)
        self.parent = parent
        self.cost = cost  # CSF(n)

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __lt__(self, other):
        return self.cost < other.cost
