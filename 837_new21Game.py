# Problem 827. New 21 Game
# Alice plays the following game, loosely based on the card game "21".

# Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an
# integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent 
# and the outcomes have equal probabilities.

# Alice stops drawing numbers when she gets k or more points.

# Return the probability that Alice has n or fewer points.

# Answers within 10-5 of the actual answer are considered accepted.

def new21Game(n, k, maxPoints):
    # Base cases
    if (n - maxPoints) >= k or k == 0:
        return 1.0



print(new21Game(10, 1, 10))
print(new21Game(6, 1, 10))
print(new21Game(21, 17, 10))

# Example 1:
# Input: n = 10, k = 1, maxPts = 10
# Output: 1.00000

# Example 2:
# Input: n = 6, k = 1, maxPts = 10
# Output: 0.60000

# Example 3:
# Input: n = 21, k = 17, maxPts = 10
# Output: 0.73278