# Solution to 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer
# range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

def reverse(x):
    isNegative = True if x < 0 else False

    max = 2 ** 32 - 1
    min = -2 ** 32

    reversed = str(abs(x))[::-1]
    negChar = "-"

    if isNegative:
        output = int(negChar + reversed)
    else:
        output = int(reversed)

    if output < min or output > max:
        return 0

    return output


val = -120
print(reverse(val))