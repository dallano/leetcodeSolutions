# Solution to 29. Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using multiplication,
# division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part.
# For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the
# 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly
# greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231,
# then return -231.

def divide(dividend, divisor):
    maxLimit = 2 ** 32 - 1
    minLimit = -2 ** 32
    ans = len(range(0, abs(dividend)-abs(divisor) + 1, abs(divisor)))

    # If 1 value is negative, our result will be negative
    if (dividend < 0) ^ (divisor < 0):
        ans = -ans

    return min(max(minLimit, ans), maxLimit)

# Test Cases
dividend1 = 10
divisor1 = 3

dividend2 = 7
divisor2 = -3

print(divide(dividend2, divisor2))