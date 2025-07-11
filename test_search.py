# test_search.py
# tests each of the three search algorithms to confirm they are working
# prints the solved maze to the console
# prints time taken by each algorithm

import time
from maze import generate_maze, START, TREASURE
from search import bfs, dfs, a_star


def find_position(maze, symbol):
    """
    Helper function to find the (row, col) of a symbol in the maze.
    """
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == symbol:
                return (r, c)
    return None


def print_maze_with_path(maze, path):
    """
    Prints the maze with the path marked using 'X'.
    """
    maze_copy = [row.copy() for row in maze]  # Deep copy to preserve original

    for position in path:
        r, c = position
        if maze_copy[r][c] == ".":
            maze_copy[r][c] = "X"  # Mark path

    for row in maze_copy:
        print(" ".join(row))


def test_search_algorithm(name, search_fn):
    """
    Runs a search algorithm, prints results, and prints execution time.
    """
    print(f"\n--- Testing {name} ---")
    maze = generate_maze()
    start = find_position(maze, START)
    treasure = find_position(maze, TREASURE)

    start_time = time.time()  # start of algorithm
    path = search_fn(maze, start, treasure)
    end_time = time.time()  # end of algorithm

    duration = end_time - start_time

    if path:
        print(f"Path to treasure found! Steps: {len(path) - 1}")
        print_maze_with_path(maze, path)
    else:
        print("No path to treasure found.")

    print(f"Time taken: {duration:.6f} seconds")


if __name__ == "__main__":
    test_search_algorithm("Breadth-First Search (BFS)", bfs)
    test_search_algorithm("Depth-First Search (DFS)", dfs)
    test_search_algorithm("A* Search", a_star)
