# search.py
# BFS, DFS, and A* implementations

from collections import deque
from maze import *
import heapq


def bfs(maze, start_pos, treasure_pos):
    """
    BFS explores the maze level by level
    and guarantees the shortest path in terms of number of steps.
    """
    start_node = Node(start_pos)
    frontier = deque([start_node])  # BFS requires a queue
    visited = set()

    while frontier:
        current_node = frontier.popleft()  # dequeue the next node to explore

        # check if we've found the treasure
        if current_node.position == treasure_pos:
            return reconstruct_path(current_node)

        if current_node.position in visited:
            continue  # skip already visited positions

        visited.add(current_node.position)

        # explore neighbors (up, down, left, right)
        for neighbor_pos in get_neighbors(current_node.position, maze):
            if neighbor_pos not in visited:
                neighbor_node = Node(neighbor_pos, parent=current_node)
                frontier.append(neighbor_node)

    return None  # no path to treasure found


def dfs(maze, start_pos, treasure_pos):
    """
    DFS explores deeply along each path before backtracking.
    It is not guaranteed to find the shortest path.
    """
    start_node = Node(start_pos)
    frontier = [start_node]  # DFS requires a stack
    visited = set()

    while frontier:
        current_node = frontier.pop()

        # check if we've reached the treasure
        if current_node.position == treasure_pos:
            return reconstruct_path(current_node)

        if current_node.position in visited:
            continue

        visited.add(current_node.position)

        # add valid neighbors to the stack
        for neighbor_pos in get_neighbors(current_node.position, maze):
            if neighbor_pos not in visited:
                neighbor_node = Node(neighbor_pos, parent=current_node)
                frontier.append(neighbor_node)

    return None  # no path to treasure found


from utils import *


def a_star(maze, start_pos, treasure_pos):
    """
    A* finds the shortest path using a combination of cost so far (CSF)
    and estimated cost to go (CTG). It is efficient and optimal when using
    a heuristic like the Manhattan distance.
    f(n) = CSF(n) + CTG(n)
    """
    start_node = Node(start_pos, cost=0)
    frontier = [(0, start_node)]  # priority queue: (f(n), node)
    visited = set()

    while frontier:
        _, current_node = heapq.heappop(frontier)  # get node with lowest f(n)

        # check if treasure is found
        if current_node.position == treasure_pos:
            return reconstruct_path(current_node)

        if current_node.position in visited:
            continue

        visited.add(current_node.position)

        # explore neighbors
        for neighbor_pos in get_neighbors(current_node.position, maze):
            if neighbor_pos not in visited:
                cost_so_far = current_node.cost + 1  # CSF
                cost_to_go = manhattan_distance(
                    neighbor_pos, treasure_pos
                )  # estimated CTG
                f_cost = cost_so_far + cost_to_go  # total estimated cost
                neighbor_node = Node(
                    neighbor_pos, parent=current_node, cost=cost_so_far
                )
                heapq.heappush(frontier, (f_cost, neighbor_node))

    return None  # no path to treasure found
