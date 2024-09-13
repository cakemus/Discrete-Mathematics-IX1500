import math
import itertools
import matplotlib.pyplot as plt

start_point = (0, 3)
end_point = (7, 2)

def binomial_coefficient(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def calc_total_paths(start_point, end_point):
    x1, y1 = start_point
    x2, y2 = end_point

    #total nr of moves
    total_moves = x2 - x1
    #moves up (U)
    upward_moves = (total_moves + (y2 - y1)) // 2
    #moves down (L)
    downward_moves = total_moves - upward_moves
    #total number of paths
    total_paths = binomial_coefficient(total_moves, upward_moves)
    return total_paths

def UL_combinations():
    moves = ['U'] * 3 + ['L'] * 4  # 3 U's and 4 L's
    unique_paths = set(itertools.permutations(moves))  # Generate all unique permutations
    
    return unique_paths

total_paths = calc_total_paths(start_point, end_point)
print(f"Total paths from point {start_point} to point {end_point}: {total_paths}")
unique_paths = UL_combinations()


sorted_paths = [''.join(path) for path in unique_paths]
sorted_paths.sort()
n = 0
for path in sorted_paths:
    path_str = ''.join(path)
    n += 1    
    print(f"{path_str} {n}")