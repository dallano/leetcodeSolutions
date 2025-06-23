def plusOne(digits):
    newList = []
    s = ""

    for num in digits:
        s = s + str(num) # Convert values into a string
    
    s = str(int(s) + 1) # Convert results of integer addition into string

    for i in range(len(s)):
        newList.append(int(s[i])) # Add integer values of string into a new list

    return newList

nums = [9, 4, 3, 9, 9, 9]
print(plusOne(nums))