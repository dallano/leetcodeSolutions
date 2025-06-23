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