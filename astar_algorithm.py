import heapq
import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # (y, x)
        self.parent = parent
        self.g = 0  # Cost from start to node
        self.h = 0  # Heuristic cost to end
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.position == other.position

def heuristic(node1, node2):
    return abs(node1.position[0] - node2.position[0]) + abs(node1.position[1] - node2.position[1])

def a_star(start, end, grid):
    start_node = Node(start)
    end_node = Node(end)

    open_list = []
    closed_list = []

    heapq.heappush(open_list, (start_node.f, start_node))

    while open_list:
        current_node = heapq.heappop(open_list)[1]
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        children = []
        for new_position in [(0, -1), (0, 1), (1, 0), (-1, 0)]:  # 4 possible movements
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid) - 1]) - 1) or node_position[1] < 0:
                continue

            if grid[node_position[0]][node_position[1]] != 0:
                continue  # If not walkable

            new_node = Node(node_position, current_node)
            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = heuristic(child, end_node)
            child.f = child.g + child.h

            if not any(open_child.position == child.position and open_child.g <= child.g for open_child in open_list):
                heapq.heappush(open_list, (child.f, child))

    return []  # Return empty path if no path found

def visualize_path(grid, path):
    grid_copy = np.array(grid)
    for position in path:
        grid_copy[position[0]][position[1]] = 2  # Mark path
    plt.imshow(grid_copy, cmap='hot', interpolation='nearest')
    plt.show()

# Test with a simple grid
if __name__ == '__main__':
    grid = [[0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]]
    start = (0, 0)
    end = (4, 4)
    path = a_star(start, end, grid)
    print('Path:', path)
    visualize_path(grid, path)