# main.py
import time
from maze import generate_maze, START, TREASURE, get_neighbors, reconstruct_path
from search import bfs, dfs, a_star
from utils import manhattan_distance  # if needed

import os


def find_position(maze, symbol):
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == symbol:
                return (r, c)
    return None


def print_maze(maze, frontier=set(), visited=set(), path=None):
    display = [row.copy() for row in maze]

    for r, c in visited:
        if display[r][c] == ".":
            display[r][c] = "@"

    for r, c in frontier:
        if display[r][c] == ".":
            display[r][c] = "+"

    if path:
        for r, c in path:
            if display[r][c] in {".", "@", "+"}:
                display[r][c] = "*"

    os.system("clear" if os.name == "posix" else "cls")
    for row in display:
        print(" ".join(row))
    print()


def run_search_with_visualization(maze, algorithm_fn, delay=0.1):
    start = find_position(maze, START)
    treasure = find_position(maze, TREASURE)

    frontier = []
    visited = set()
    path = []

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

    while frontier:
        # Get next node
        if algorithm_fn == bfs:
            current_node = frontier.popleft()
        elif algorithm_fn == dfs:
            current_node = frontier.pop()
        elif algorithm_fn == a_star:
            _, current_node = heapq.heappop(frontier)

        pos = current_node.position

        if pos == treasure:
            path = reconstruct_path(current_node)
            break

        if pos in visited:
            continue

        visited.add(pos)

        # Add neighbors
        for neighbor_pos in get_neighbors(pos, maze):
            if neighbor_pos not in visited:
                neighbor_node = Node(neighbor_pos, parent=current_node)
                if algorithm_fn == bfs:
                    frontier.append(neighbor_node)
                elif algorithm_fn == dfs:
                    frontier.append(neighbor_node)
                elif algorithm_fn == a_star:
                    import heapq

                    g = current_node.cost + 1
                    h = manhattan_distance(neighbor_pos, treasure)
                    f = g + h
                    neighbor_node.cost = g
                    heapq.heappush(frontier, (f, neighbor_node))

        # Visualization step
        frontier_positions = [
            n.position if not isinstance(n, tuple) else n[1].position for n in frontier
        ]
        print_maze(maze, frontier=set(frontier_positions), visited=visited)
        time.sleep(delay)

    # Final maze with path
    print_maze(maze, visited=visited, path=path)
    print(f"Path length: {len(path) - 1 if path else 'N/A'}")


if __name__ == "__main__":
    from maze import Node

    maze = generate_maze()

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
