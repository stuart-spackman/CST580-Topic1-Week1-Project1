# test_maze.py
from maze import generate_maze, get_neighbors, Node, reconstruct_path


def test_generate_maze():
    maze = generate_maze()
    print("Maze:")
    for row in maze:
        print(" ".join(row))


def test_get_neighbors():
    maze = generate_maze()
    print("\nTesting get_neighbors() from (0,1):")
    neighbors = get_neighbors((0, 1), maze)
    print("Expected: [(0, 2)] or similar depending on layout")
    print("Actual:", neighbors)

    print("\nTesting get_neighbors() from (2,2):")
    neighbors = get_neighbors((2, 2), maze)
    print("Expected: Four directions unless blocked by wall")
    print("Actual:", neighbors)


def test_reconstruct_path():
    print("\nTesting reconstruct_path():")
    # Simulate a short path: start -> (0,1) -> (1,1) -> (2,1)
    node3 = Node((2, 1))
    node2 = Node((1, 1), parent=node3)
    node1 = Node((0, 1), parent=node2)
    start = Node((0, 0), parent=node1)

    path = reconstruct_path(start)
    print("Expected path: [(2, 1), (1, 1), (0, 1), (0, 0)]")
    print("Actual path:", path)


if __name__ == "__main__":
    test_generate_maze()
    test_get_neighbors()
    test_reconstruct_path()
