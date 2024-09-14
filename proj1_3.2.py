import math
import itertools
import matplotlib.pyplot as plt

a_votes = 9
b_votes = 2

def L(m, n):
    return (m+1, n-1)
def U(m, n):
    return (m+1, n+1)

def binomial_coefficient(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def ballot_theorem(a, b):
    if a <= b:
        return 0 #invalid, a cannot always be ahead of b
    
    #ballot theorem, probability that a is strictly ahead of b, given that a > b = (a-b)/(a+b)
    probability = ((a - b)) / (a + b)
    
    total_ways = binomial_coefficient(a + b, b)
    valid_ways = total_ways * probability

    return probability, total_ways, valid_ways

#produces all combinations of UL-paths possible
def ul_combinations():
    moves = ['U'] * 9 + ['L'] * 2  # 9 U's and 2 L's
    unique_paths = set(itertools.permutations(moves))  # Generate all unique permutations
    
    return unique_paths

#makes UL path into x,y path
def ul_to_coords(path):
    """
    Simulates the path based on the sequence of moves ('U' and 'L') 
    and returns the list of coordinates.
    """
    #start at (0, 0)
    x, y = 0, 0
    coordinates = [(x, y)]  #start coordinate
    
    #apply each move in the path
    for move in path:
        if move == 'U':
            x, y = U(x, y)  #use U function to move up
        elif move == 'L':
            x, y = L(x, y)  #use L function to move down
        coordinates.append((x, y))  #add the new coordinates
    
    return coordinates

def isolate_paths(combinations):
    """
    Returns only the paths where y is never equal to 0 for any x-coordinate, 
    excluding the starting point (0, 0).
    """
    return [ul_to_coords(path) for path in combinations if all(y != 0 for x, y in ul_to_coords(path)[1:])]

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


probability, total_ways, valid_ways = ballot_theorem(a_votes, b_votes)

print(f"There are {valid_ways} ways that A is always ahead of B, out of {total_ways} total ways")
print(f"The probability that A is always ahead of B is {(probability) * 100:.2f}%")

ul_paths = ul_combinations()
isolated_paths = isolate_paths(ul_paths)

n = 1  
for path in isolated_paths:
    path_str = " -> ".join([f"({x},{y})" for x, y in path])
    print(f"{path_str} n = {n}")
    n += 1

plot_paths(isolated_paths)