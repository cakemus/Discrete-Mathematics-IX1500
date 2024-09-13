import math
import itertools
import matplotlib.pyplot as plt

start_point = (0, 3)
end_point = (7, 2)

def L(m, n):
    return (m+1, n-1)
def U(m, n):
    return (m+1, n+1)

def binomial_coefficient(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))



def calc_total_paths(start_point, end_point):
    x1, y1 = start_point
    x2, y2 = end_point

    #total nr of moves
    total_moves = x2 - x1
    #moves up (U)
    upward_moves = (total_moves + (y2 - y1)) // 2
    #total number of paths
    total_paths = binomial_coefficient(total_moves, upward_moves)
    return total_paths

def ul_combinations():
    moves = ['U'] * 3 + ['L'] * 4  # 3 U's and 4 L's
    unique_paths = set(itertools.permutations(moves))  # Generate all unique permutations
    
    return unique_paths
 
#makes UL path into x,y path
def ul_to_coords(path):
    """
    Simulates the path based on the sequence of moves ('U' and 'L') 
    and returns the list of coordinates.
    """
    # Start at (0, 3)
    x, y = 0, 3
    coordinates = [(x, y)]  # Start coordinate
    
    # Apply each move in the path
    for move in path:
        if move == 'U':
            x, y = U(x, y)  # Use U function to move up
        elif move == 'L':
            x, y = L(x, y)  # Use L function to move down
        coordinates.append((x, y))  # Add the new coordinates
    
    return coordinates

def isolate_paths(combinations):
    # Use list comprehension to simulate paths and check if they cross (3,0) or (5,0)
    return [ul_to_coords(path) for path in combinations if (3, 0) in ul_to_coords(path) or (5, 0) in ul_to_coords(path)]

def plot_paths(paths):
    plt.figure(figsize=(10, 6))  # Set the figure size

    # Plot each path
    for path in paths:
        x_values, y_values = zip(*path)  # Separate x and y coordinates
        plt.plot(x_values, y_values, marker='o')

    # Configure the plot's appearance
    plt.title("Valid paths not crossing the x-axis")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()  # Display the plot

total_paths = calc_total_paths(start_point, end_point)
#andre's reflection principle
reflection = (end_point[0], -end_point[1])
#using reflection as end point we calculate total nr of points that do reach x-axis
valid_paths = calc_total_paths(start_point, reflection)
invalid_paths = total_paths - valid_paths
ul_paths = ul_combinations()
isolated_paths = isolate_paths(ul_paths)

print(f"Total paths from point {start_point} to point {end_point}: {total_paths}")
print(f"Number of invalid paths: {invalid_paths}")
print(f"Number of valid paths: {valid_paths}")

n = 1  
for path in isolated_paths:
    path_str = " -> ".join([f"({x},{y})" for x, y in path])
    print(f"{path_str} n = {n}")
    n += 1

plot_paths(isolated_paths)