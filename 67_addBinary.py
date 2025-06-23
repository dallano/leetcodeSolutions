# Solution to 67. Add Binary

def addBinary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

bin1 = "10001101"
bin2 = "00101111"

print(addBinary(bin1, bin2))