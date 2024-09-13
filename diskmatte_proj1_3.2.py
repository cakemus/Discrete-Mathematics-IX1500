import math

def binomial_coefficient(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def ballot_theorem(a, b):
    if a <= b:
        return 0 #invalid, a cannot always be ahead of b
    
    total_ways = binomial_coefficient(a + b, b)
    valid_ways = ((a - b) * total_ways) / (a + b)
    
    return valid_ways, total_ways

def probability_a_always_ahead(a, b):
    valid_ways, total_ways = ballot_theorem(a, b)
    probability = valid_ways / total_ways

    return valid_ways, total_ways, probability

a_votes = 9
b_votes = 2

valid_ways, total_ways, probability = probability_a_always_ahead(a_votes, b_votes)

print(f"There are {valid_ways} ways that A is always ahead of B, out of {total_ways} total ways")
print(f"The probability that A is always ahead of B is {(valid_ways / total_ways) * 100:.2f}%")