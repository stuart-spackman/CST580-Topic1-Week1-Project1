# main.py
# runs all 3 search algorithms on the maze in maze.py
# uses matplotlib to visualize solving progress

import time
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# import required functions and constants from other files
from maze import generate_maze, START, TREASURE, get_neighbors, reconstruct_path, Node
from search import bfs, dfs, a_star
from utils import manhattan_distance  # used by A*


# helper to locate the coordinates of a symbol in the maze (like 'S' or 'T')
def find_position(maze, symbol):
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == symbol:
                return (r, c)
    return None


# converts the maze into a 2D array of numeric codes for visualization
def maze_to_array(maze, frontier=set(), visited=set(), path=None):
    symbol_map = {
        "#": 0,  # wall
        ".": 1,  # empty space
        "S": 2,  # start
        "T": 3,  # treasure (goal)
    }

    rows, cols = len(maze), len(maze[0])
    array = [[symbol_map.get(cell, 1) for cell in row] for row in maze]

    # mark visited nodes in the array
    for r, c in visited:
        if maze[r][c] == ".":
            array[r][c] = 4

    # mark frontier (nodes about to be explored)
    for r, c in frontier:
        if maze[r][c] == ".":
            array[r][c] = 5

    # mark final path if known
    if path:
        for r, c in path:
            if maze[r][c] in {".", "S", "T"}:
                array[r][c] = 6

    return array


# renders the maze visually using matplotlib
def visualize_maze(maze, frontier=set(), visited=set(), path=None):
    data = maze_to_array(maze, frontier, visited, path)

    # Create a custom color map
    cmap = mcolors.ListedColormap(
        [
            "black",  # 0 - wall
            "white",  # 1 - empty
            "green",  # 2 - start
            "red",  # 3 - treasure
            "lightgray",  # 4 - visited
            "blue",  # 5 - frontier
            "gold",  # 6 - path
        ]
    )

    plt.clf()  # Clear previous frame
    plt.imshow(data, cmap=cmap)  # Show current state
    # plt.axis("off")  # Hide axis ticks
    plt.pause(0.01)  # Brief pause to allow for animation


# Main loop that runs the selected search algorithm with step-by-step visualization
def run_search_with_visualization(maze, algorithm_fn, delay=0.05):
    start = find_position(maze, START)
    treasure = find_position(maze, TREASURE)

    visited = set()  # Keep track of explored positions
    path = []  # Final path from start to treasure (if found)

    # Choose the correct data structure for the frontier based on the algorithm
    if algorithm_fn == bfs:
        from collections import deque

        frontier = deque([Node(start)])
    elif algorithm_fn == dfs:
        frontier = [Node(start)]
    elif algorithm_fn == a_star:
        import heapq

        frontier = []
        heapq.heappush(frontier, (0, Node(start)))
    else:
        print("Unknown search function")
        return

    plt.figure(figsize=(8, 8))  # Set up visualization window

    # Main search loop
    while frontier:
        # Get next node from the frontier
        if algorithm_fn == bfs:
            current_node = frontier.popleft()
        elif algorithm_fn == dfs:
            current_node = frontier.pop()
        elif algorithm_fn == a_star:
            _, current_node = heapq.heappop(frontier)

        pos = current_node.position

        # If treasure is found, reconstruct the path and break
        if pos == treasure:
            path = reconstruct_path(current_node)
            break

        if pos in visited:
            continue

        visited.add(pos)

        # Expand neighbors
        for neighbor_pos in get_neighbors(pos, maze):
            if neighbor_pos not in visited:
                neighbor_node = Node(neighbor_pos, parent=current_node)

                if algorithm_fn == bfs or algorithm_fn == dfs:
                    frontier.append(neighbor_node)
                elif algorithm_fn == a_star:
                    g = current_node.cost + 1  # Cost so far
                    h = manhattan_distance(neighbor_pos, treasure)  # Heuristic
                    f = g + h  # Total estimated cost
                    neighbor_node.cost = g
                    heapq.heappush(frontier, (f, neighbor_node))

        # Prepare the list of frontier positions (depends on structure type)
        frontier_positions = [
            n.position if not isinstance(n, tuple) else n[1].position for n in frontier
        ]

        # Update visualization with current state
        visualize_maze(maze, frontier=set(frontier_positions), visited=visited)
        time.sleep(delay)

    # Final visualization including path (if found)
    visualize_maze(maze, visited=visited, path=path)
    print(f"Path length: {len(path) - 1 if path else 'N/A'}")
    plt.show()  # Keep final frame open


# Entry point
if __name__ == "__main__":
    maze = generate_maze()

    # User selects search algorithm
    print("Choose search algorithm:")
    print("1. BFS")
    print("2. DFS")
    print("3. A*")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        run_search_with_visualization(maze, bfs)
    elif choice == "2":
        run_search_with_visualization(maze, dfs)
    elif choice == "3":
        run_search_with_visualization(maze, a_star)
    else:
        print("Invalid choice.")
