import math

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


total_paths = calc_total_paths(start_point, end_point)
#andre's reflection principle
reflection = (end_point[0], -end_point[1])
#using reflection as end point we calculate total nr of points that do reach x-axis
invalid_paths = calc_total_paths(start_point, reflection)
valid_paths = total_paths - invalid_paths



print(f"Total paths: {total_paths}")
print(f"Invalid paths: {invalid_paths}")
print(f"Valid paths {valid_paths}")



    

