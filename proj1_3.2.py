import math

a_votes = 9
b_votes = 2

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



probability, total_ways, valid_ways = ballot_theorem(a_votes, b_votes)

print(f"There are {valid_ways} ways that A is always ahead of B, out of {total_ways} total ways")
print(f"The probability that A is always ahead of B is {(probability) * 100:.2f}%")