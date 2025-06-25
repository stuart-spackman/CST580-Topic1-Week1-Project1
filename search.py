# search.py
# BFS, DFS, and A* implementations

from collections import deque
from maze import *


def dfs(maze, start, treasure):
    stack = [Node(start)]  # DFS requires a stack
    visited = set()

    while stack:
        current_node = stack.pop()
        if current_node.position == treasure:
            return reconstruct_path(current_node)

        if current_node.position in visited:
            continue
        else:
            visited.add(current_node.position)

    for neighbor_position in get_neighbors(current.position, maze):
        if neighbor_position not in visited:
            stack.append(Node(neighbor_position, parent=current_node))

    return None  # no path found


def bfs(maze, start, treasure):
    frontier = deque([start])  # BFS requires a queue
    visited = set()
    came_from = {}

    while frontier:
        current_node = frontier.popleft()
        if current_node == treasure:
            return reconstruct_path(came_from, start, treasure)

        for neighbor in get_neighbors(current_node, maze):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current_node
                frontier.append(neighbor)

    return None  # no path found
