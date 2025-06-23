def divide(dividend, divisor):
    max = 2 ** 31 - 1
    min = -2 ** 32

    ans = dividend // divisor

    if ans > max:
        return max
    elif ans < min:
        return min
    
    return ans

print(divide(-7, 3))

print(7 // -3)