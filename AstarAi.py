import heapq
import matplotlib.pyplot as plt
import numpy as np

# 1. Heuristic Function (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 2. A* Algorithm Core
def a_star(grid, start, goal):
    rows, cols = grid.shape
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Priority Queue: (priority, current_cost, current_node, path)
    pq = [(0 + heuristic(start, goal), 0, start, [start])]
    visited = {} # node: min_cost_to_reach

    while pq:
        f_score, g_score, current, path = heapq.heappop(pq)

        if current == goal:
            return path, g_score

        if current in visited and visited[current] <= g_score:
            continue
        visited[current] = g_score

        for dr, dc in neighbors:
            neighbor = (current[0] + dr, current[1] + dc)
            
            # Check boundaries and obstacles (1 = wall)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 0:
                    new_g = g_score + 1 # Uniform cost
                    new_f = new_g + heuristic(neighbor, goal)
                    heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
    
    return None, float('inf')

# 3. Visualization Function
def visualize_path(grid, path, start, goal, title="A* Pathfinding"):
    grid_copy = np.array(grid, dtype=float)
    
    # Plotting setup
    plt.figure(figsize=(8, 8))
    plt.imshow(grid_copy, cmap='Greys', origin='upper')
    
    if path:
        path_x = [p[1] for p in path]
        path_y = [p[0] for p in path]
        plt.plot(path_x, path_y, color='red', linewidth=2, label="Shortest Path")
    
    plt.scatter(start[1], start[0], color='green', s=100, label="Start", zorder=5)
    plt.scatter(goal[1], goal[0], color='blue', s=100, label="Goal", zorder=5)
    
    plt.title(title)
    plt.legend()
    plt.grid(True, which='both', color='lightgrey', linestyle='-', linewidth=0.5)
    plt.show()

# --- TEST CASES ---

# Case 1: Simple Maze
grid1 = np.zeros((10, 10))
grid1[3, 0:7] = 1 # Horizontal wall
start1, goal1 = (0, 0), (9, 9)

# Case 2: Narrow Corridor
grid2 = np.zeros((10, 10))
grid2[0:8, 5] = 1
grid2[2:10, 7] = 1
start2, goal2 = (0, 0), (9, 9)

# Case 3: No Path (Obstacle blocking goal)
grid3 = np.zeros((5, 5))
grid3[0, 1] = 1
grid3[1, 0] = 1
start3, goal3 = (0, 0), (4, 4)

tests = [(grid1, start1, goal1, "Test 1: Standard Maze"), 
         (grid2, start2, goal2, "Test 2: Narrow Corridor"),
         (grid3, start3, goal3, "Test 3: Unreachable Goal")]

for g, s, goal, t in tests:
    path, cost = a_star(g, s, goal)
    print(f"{t} - Path Cost: {cost}")
    visualize_path(g, path, s, goal, t)