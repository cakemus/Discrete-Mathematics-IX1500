import math
import itertools
import matplotlib.pyplot as plt

start_point = (7, 6)
end_point = (20, 5)

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
    moves = ['U'] * 6 + ['L'] * 7  # 3 U's and 4 L's
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

total_paths = calc_total_paths(start_point, end_point)
#andre's reflection principle
reflection = (start_point[0], -start_point[1])
#using reflection as start point we calculate total nr of points that do reach x-axis
invalid_paths = calc_total_paths(reflection, end_point)
valid_paths = total_paths - invalid_paths



print(f"Total paths: {total_paths}")
print(f"Invalid paths: {invalid_paths}")
print(f"Valid paths {valid_paths}")



    

